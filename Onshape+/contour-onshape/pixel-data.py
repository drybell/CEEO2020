from PIL import Image
import matplotlib.pyplot as plt
from onshape_client.client import Client 
import json
from math import floor
from random import randint
import sys
from sklearn.neighbors import NearestNeighbors
import networkx as nx
import numpy as np 
sys.setrecursionlimit(100000)

# first point should be last point, add first point to end of string

key = ""
secret = ""

with open("../scripts/api-key", "r") as f: 
	key = f.readline().rstrip()
	secret = f.readline().rstrip()

base_url = 'https://rogers.onshape.com'

client = Client(configuration={"base_url": base_url, "access_key": key, "secret_key": secret})

did = "aec16876714d70a447e5b140"
wid = "c96b1b15861efbe1cf7dd9be"
# eid = "db62cec33be087b52f777ec3"
eid = "92e70961b3ada9cd69667064"

get_string = "/api/featurestudios/d/aec16876714d70a447e5b140/w/c96b1b15861efbe1cf7dd9be/e/92e70961b3ada9cd69667064"
update_string = "/api/featurestudios/d/aec16876714d70a447e5b140/w/c96b1b15861efbe1cf7dd9be/e/92e70961b3ada9cd69667064"
post_api_call = base_url + update_string
get_api_call = base_url + get_string

image = Image.open('complex-high.jpg') 
f = image.load() 

color = 5
scale = 100 #.1 scale

pixels = []
test_array = []

# For each Canny Contour, follow its line and make it its own sketch, 
# We can split them up into lines so FeatureScript doesn't get confused
# I need to standardize the way canny-jpgs get created and find a 
# resolution that doesn't kill an Onshape workspace 

# Another idea, just use a square with set width/height and iterate through 
# the image, if something's black make it a point. Lowers the resolution

# or a lookback? 

scanner_box = 4 # set the window to be 2 x 2 px 

for x in range(image.size[0]):
	temp = []
	for y in range(image.size[1]):
		# Average the window's pixels to one color 
		if f[x,y] <= color:
			pixels.append([x,y])
			temp.append("1")
		else:
			temp.append("0")
	test_array.append(temp)

print("Max x: %d" % (image.size[0]))
print("Max y: %d" % (image.size[1]))


# For higher resolution images, let's try to just grab the outer pixels of the 
# shaded region and work from there 

# To do that, we iterate from all 4 sides of the image and attempt to reach the 
# center of the image. 
# If we reach a pixel, we take its position and move on
# Purge duplicate positions after 
def gatherOuterPoints(plot):
	max_x = len(plot)
	max_y = len(plot[0])
	outer_pixels = []

	# Top down = for each x array, iterate through y arrays + and find first 1 
	for x in range(max_x):
		for y in range(max_y): 
			if plot[x][y] == "1":
				outer_pixels.append([x,y])
				break

	# Left right = for each position in y, iterate through the same position of x
	for y in range(max_y): 
		for x in range(max_x):
			if plot[x][y] == "1":
				outer_pixels.append([x,y])
				break

	# Down up = At the ends of each y, count down until you reach a 1 
	for x in range(max_x):
		for y in range(max_y - 1, -1, -1):
			if plot[x][y] == "1":
				outer_pixels.append([x,y])
				break

	#Right left = At the ends of x, count backwards through x 
	for y in range(max_y -1, -1, -1):
		for x in range(max_x - 1, -1, -1): 
			if plot[x][y] == "1":
				outer_pixels.append([x,y])
				break

	purged = []
	for item in outer_pixels:
		if item not in purged: 
			purged.append(item)

	return purged

# for each N x N region of the plot, average the internal 1 positions
def averagebyN(N, plot): 
	offset_x = N
	offset_y = N 

	max_x = len(plot)
	max_y = len(plot[0])

	# I don't think I'll care about the ends since N will generally be small
	remainder_x = max_x % offset_x
	remainder_y = max_y % offset_y

	averaged_pixels = []

	for x in range(0, max_x - remainder_x, offset_x):
		for y in range(0, max_y - remainder_y, offset_y):
			count = 0
			one_positions = []
			for i in range(offset_x):
				for j in range(offset_y): 
					if plot[x + i][y + j] == "1": 
						count += 1
						one_positions.append([x + i,y + j])
			if count == 0: 
				continue
			sum_x = 0
			sum_y = 0
			for coords in one_positions:
				sum_x += coords[0]
				sum_y += coords[1]

			new_coords = [floor(sum_x/count), floor(sum_y/count)]
			averaged_pixels.append(new_coords)

	return averaged_pixels

def outOfBounds(x,y,max_x,max_y):
	return x < 0 or x >= max_x or y < 0 or y >= max_y

def gatherNeighbors(directions, plot, index):
	max_y = len(plot[0])
	max_x = len(plot)
	neighbors = {}
	totals = 0
	for key in directions:
		direction = directions[key]
		new_x = index[0] + direction[0]
		new_y = index[1] + direction[1]
		if outOfBounds(new_x,new_y, max_x, max_y):
			continue
		else: 
			if plot[new_x][new_y] == "1":
				neighbors.update({key: [new_x, new_y]})
				totals += 1
				# print(neighbors)
	return neighbors, totals

def allInDirection(direction, plot, index): 
	directions = {"n": [0,-1], "ne": [1,-1], "nw": [-1,-1], "e": [1,0], "se": [1,1], "sw": [-1,1], "s": [0,1], "w": [-1,0]}
	direction = directions[direction]
	temp = []
	flag = False
	curr = [index[0] + direction[0], index[1] + direction[1]]
	while not outOfBounds(curr[0], curr[1], len(plot), len(plot[0])):
		# print(plot[curr[0]][curr[1]])
		if plot[curr[0]][curr[1]] == "1":
			temp.append(curr)
			curr = [curr[0] + direction[0], curr[1] + direction[1]]
		else: 
			break

	# print(temp)
	if len(temp) == 0:
		return [-1,-1]
	else:
		return temp[-1]

def reducePoints(plot):
	directions = {"n": [0,-1], "ne": [1,-1], "nw": [-1,-1], "e": [1,0], "se": [1,1], "sw": [-1,1], "s": [0,1], "w": [-1,0]}
	reduced = []
	for i in range(len(plot)): 
		for j in range(len(plot[0])):
			if plot[i][j] == "1":
				ns, totals = gatherNeighbors(directions, plot, [i,j])
				counter = 0
				for n in ns: 
					temp = allInDirection(n, plot, [ns[n][0], ns[n][1]])
					if temp != [-1,-1]:
						i = temp[0]
						j = temp[1]
						reduced.append([i,j])
	return reduced

def followOuterLine(start, curr, prev, plot, directions, gathered): 
	# if curr == start and len(gathered) > 10:
	# 	print(gathered)
	# 	return gathered
	if curr == start and len(gathered) > 500:
		return gathered
	else: 
		# print("START: %s CURR: %s PREV: %s" % (start, curr, prev))
		# print(gathered)
		ns, totals = gatherNeighbors(directions, plot, curr)
		all_totals = []
		all_neighbors = []
		for n in ns: 
			new_ns, temp_totals = gatherNeighbors(directions, plot, ns[n])
			all_totals.append(temp_totals)
			all_neighbors.append(ns[n])

		# first attempt
		least_neighbor = all_neighbors[all_totals.index(min(all_totals))]
		ctr = 0
		min_sorted_indices = [i[0] for i in sorted(enumerate(all_totals), key=lambda x:x[1])]
		print("MIN SORTED: %s" % (min_sorted_indices))
		print("ALL NEIGHBORS: %s" % (all_neighbors))
		print("ALL TOTALS: %s" % (all_totals))
		while least_neighbor in gathered:
			least_neighbor = all_neighbors[min_sorted_indices[ctr]]	
			total = all_totals[min_sorted_indices[ctr]]	
			ctr += 1
			if ctr == len(min_sorted_indices):
				for i in range(len(min_sorted_indices), 0, -1):
					if all_totals[min_sorted_indices[i]] < 8:
						least_neighbor = all_neighbors[min_sorted_indices[i]]	
		gathered.append(least_neighbor)
		return followOuterLine(start,least_neighbor, curr, plot, directions, gathered)

def complexTravel(plot, outer_points):
	reduced = []
	directions = {"n": [0,-1], "ne": [1,-1], "nw": [-1,-1], "e": [1,0], "se": [1,1], "sw": [-1,1], "s": [0,1], "w": [-1,0]}
	# begin by attempting to grab outer points 
	outer_pixels = gatherOuterPoints(plot)
	# grab a random point to start our traversal
	totals = 5
	rand_tries = []
	ns = {}
	start = []
	test_index = 0
	while totals >= 5: 
		test_index = randint(0, len(outer_pixels) - 1)
		if test_index not in rand_tries:
			rand_tries.append(test_index)
		start = outer_pixels[test_index]
		ns, totals = gatherNeighbors(directions, plot, start)

	# grabbed a good point coordinate called start
	# grab its first neighbor
	next_neighbor = ns[next(iter(ns))]
	print("START %s" % (start))
	return followOuterLine(start, next_neighbor, start, plot, directions, outer_points)

def removeAll8Neighbors(plot):
	directions = {"n": [0,-1], "ne": [1,-1], "nw": [-1,-1], "e": [1,0], "se": [1,1], "sw": [-1,1], "s": [0,1], "w": [-1,0]}
	reduced = []
	for x in range(len(plot)):
		for y in range(len(plot[0])):
			ns, totals = gatherNeighbors(directions, plot, [x,y])
			if totals < 6 and plot[x][y] == "1": 
				reduced.append([x,y])
	return reduced

def buildPlot(points, x_length, y_length):
	refilled = []
	for x in range(x_length):
		temp = []
		for y in range(y_length): 
			temp.append("0")
		refilled.append(temp)

	for coords in points: 
		refilled[coords[0]][coords[1]] = "1"

	return refilled

# test = []
# test = complexTravel(test_array, test)
# print(test)
test = []
with open("test-test.txt", "r") as f:
	lines = f.read().splitlines()
	for line in lines: 
		line = line.split(" ")
		test.append([int(line[0]), int(line[1])])

x = [sub[0]/scale for sub in test]
y = [sub[1]/scale for sub in test]
# plt.scatter(x, y)
# plt.show()

# outer_pixels2 = averagebyN(5, buildPlot(pixels, image.size[0], image.size[1]))
# outer_pixels1 = averagebyN(30, buildPlot(outer_pixels2, image.size[0], image.size[1]))
# outer_pixels = averagebyN(45, buildPlot(outer_pixels1, image.size[0], image.size[1]))

# # x = np.array([sub[0] for sub in outer_pixels2])
# # y = np.array([sub[1] for sub in outer_pixels2])
# test_neighbors = np.c_[x,y]
# clf = NearestNeighbors(2).fit(test_neighbors)
# G = clf.kneighbors_graph()
# T = nx.from_scipy_sparse_matrix(G)
# paths = [list(nx.dfs_preorder_nodes(T, i)) for i in range(len(test_neighbors))]

# mindist = np.inf
# minidx = 0

# for i in range(len(test_neighbors)):
# 	p = paths[i]           # order of nodes
# 	ordered = test_neighbors[p]    # ordered nodes
# 	# find cost of that order by the sum of euclidean distances between points (i) and (i+1)
# 	cost = (((ordered[:-1] - ordered[1:])**2).sum(1)).sum()
# 	if cost < mindist:
# 		mindist = cost
# 		minidx = i

# opt_order = paths[minidx]
# plt.plot(x[opt_order], y[opt_order])
# plt.show()
# exit()

# test = removeAll8Neighbors(test_array)
# averaged_pixels2 = averagebyN(10, buildPlot(test, image.size[0], image.size[1]))
# averaged_pixels1 = averagebyN(20, buildPlot(averaged_pixels2, image.size[0], image.size[1]))
# averaged_pixels = averagebyN(30, buildPlot(averaged_pixels1, image.size[0], image.size[1]))


# x0 = [sub[0]/scale for sub in test]
# y0 = [sub[1]/scale for sub in test]

# x = [sub[0]/scale for sub in averaged_pixels]
# y = [sub[1]/scale for sub in averaged_pixels]

# x_start = [sub[0]/scale for sub in outer_pixels]
# y_start = [sub[1]/scale for sub in outer_pixels]

# fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
# ax1.scatter(x0,y0)
# ax2.scatter(x,y)
# ax3.scatter(x_start,y_start)
# plt.show()
formatter_x = []
formatter_y = []
for i, pixel in enumerate(x): 
	formatter_x.append("%.6f" % (pixel))
	formatter_y.append("%.6f" % (y[i])) 

formatter_y = formatter_y[:-1]
formatter_x = formatter_x[:-1]
formatter_x.append("%.6f" % (x[0]))
formatter_y.append("%.6f" % (y[0]))

test_string = "vector( 2.000000,  1.000000) * mm"

overall_string = ""
for i in range(len(formatter_x)): 
	if i == len(formatter_x) - 1:		
		overall_string += ("vector(%s, %s) * inch" % (formatter_x[i], formatter_y[i]))
	else: 
		overall_string += ("vector(%s, %s) * inch, " % (formatter_x[i], formatter_y[i]))
	if i % 5 == 0: 
		overall_string += "\n"


# print(overall_string)

start_string = """FeatureScript 1301;
import(path : "onshape/std/geometry.fs", version : "1301.0");
annotation { "Feature Type Name" : "Python3 Feature" }
export const myFeature = defineFeature(function(context is Context, id is Id, definition is map)
	precondition
	{
		// Define the parameters of the feature type
	}
	{
		var sketch1 = newSketch(context, id + "sketch1", {
				"sketchPlane" : qCreatedBy(makeId("Top"), EntityType.FACE)
		});
		// Create sketch entities here
		skPolyline(sketch1, "polyline1", {
				"points" : ["""

end_string = """]});
		skSolve(sketch1);
// Define the function's action
	});"""

full_fs = (start_string + overall_string + end_string)

# Make API Calls
headers = {'Accept': 'application/vnd.onshape.v1+json', 'Content-Type': 'application/json'}
r = client.api_client.request('GET', url=get_api_call, query_params={}, headers=headers)
result = json.loads(r.data)
print(json.dumps(result, indent=2))

#Find rejectMicroversionSkew, serializationVersion, sourceMicroversion
serializationVersion = result["serializationVersion"]
sourceMicroversion = result["sourceMicroversion"]
rejectMicroversionSkew = result["rejectMicroversionSkew"]

body = {"contents": full_fs,
		"serializationVersion": str(serializationVersion), 
		"sourceMicroversion": str(sourceMicroversion),
		"rejectMicroversionSkew": str(rejectMicroversionSkew)}

r = client.api_client.request("POST", url=post_api_call, query_params={}, headers=headers, body=body)
result2 = json.loads(r.data)
print(json.dumps(result2, indent=2))

# print(PixelCoordinates)