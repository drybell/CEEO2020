from PIL import Image
import matplotlib.pyplot as plt
from onshape_client.client import Client 
import json

# first point should be last point, add first point to end of string

key = ""
secret = ""

with open("../api-key", "r") as f: 
	key = f.readline().rstrip()
	secret = f.readline().rstrip()

base_url = 'https://rogers.onshape.com'

client = Client(configuration={"base_url": base_url, "access_key": key, "secret_key": secret})

did = "aec16876714d70a447e5b140"
wid = "c96b1b15861efbe1cf7dd9be"
eid = "db62cec33be087b52f777ec3"

get_string = "/api/featurestudios/d/aec16876714d70a447e5b140/w/c96b1b15861efbe1cf7dd9be/e/db62cec33be087b52f777ec3"
update_string = "/api/featurestudios/d/aec16876714d70a447e5b140/w/c96b1b15861efbe1cf7dd9be/e/db62cec33be087b52f777ec3"
post_api_call = base_url + update_string
get_api_call = base_url + get_string

image = Image.open('square-small.jpg') 
f = image.load() 

color = 15
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
		temp.append("0")
	test_array.append(temp)

print("Max x: %d" % (image.size[0]))
print("Max y: %d" % (image.size[1]))

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

reduced = reducePoints(test_array)

filtered = []
new_reduced = []
# for item in reduced:
# 	if item not in filtered: 
# 		filtered.append(item)

# for item in reduced: 
# 	if item not in filtered: 
# 		temp  = allInDirection("n", test_array, item)
# 		temp2 = allInDirection("w", test_array, item)
# 		temp3 = allInDirection("e", test_array, item)
# 		temp4 = allInDirection("s", test_array, item)
# 		totals = [temp,temp2,temp3,temp4]
# 		for total in totals:
# 			if total != [-1,-1]:
# 				filtered.append(total)
# 		new_reduced.append(item)



x = [sub[0]/scale for sub in reduced]
y = [sub[1]/scale for sub in reduced]
plt.scatter(x,y)
plt.show()
exit()
formatter_x = []
formatter_y = []
for i, pixel in enumerate(x): 
	formatter_x.append("%.6f" % (pixel))
	formatter_y.append("%.6f" % (y[i])) 

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