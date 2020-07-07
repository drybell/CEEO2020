import cv2
import matplotlib.pyplot as plt
from onshape_client.client import Client 
import json
import numpy as np 


def imageToOnshape(api_path, image_path, feature_title, ids=["", "", ""], scale=100, thresh=100):

	key = ""
	secret = ""

	with open(api_path, "r") as f: 
		key = f.readline().rstrip()
		secret = f.readline().rstrip()

	did, wid, eid = ids

	base_url = 'https://rogers.onshape.com'

	client = Client(configuration={"base_url": base_url, "access_key": key, "secret_key": secret})

	get_string = "/api/featurestudios/d/" + did + "/w/" + wid + "/e/" + eid
	update_string = get_string
	post_api_call = base_url + update_string
	get_api_call = base_url + get_string

	# read the image
	img = cv2.imread(image_path)
	width = int(img.shape[1] * scale / 100)
	height = int(img.shape[0] * scale / 100)
	dim = (width, height)
	image = cv2.resize(img, dim, interpolation=cv2.INTER_NEAREST )
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

	_, binary = cv2.threshold(gray, thresh, thresh, cv2.THRESH_BINARY_INV)

	# GRAB EXTERNAL CONTOUR
	contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	data = np.vstack(contours).squeeze()
	# np.savetxt("test-test.txt", data, fmt="%d")

	x = [sub[0]/scale for sub in data]
	y = [sub[1]/scale for sub in data]

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

	start_string = start_string.replace("Python3 Feature", feature_title)

	end_string = """]});
			skSolve(sketch1);
	// Define the function's action
		});"""

	full_fs = (start_string + overall_string + end_string)

	# Make API Calls
	headers = {'Accept': 'application/vnd.onshape.v1+json', 'Content-Type': 'application/json'}
	r = client.api_client.request('GET', url=get_api_call, query_params={}, headers=headers)
	result = json.loads(r.data)

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

imageToOnshape("../scripts/api-key", "test-blocky.jpg", "From Function",ids=["aec16876714d70a447e5b140", "c96b1b15861efbe1cf7dd9be", "84bf2c49df26f1dbed74c70b"], scale=50)

