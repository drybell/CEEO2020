from onshape_client.client import Client 
from onshape_client.onshape_url import OnshapeElement
import json 

# Also need a way to port this over to a node js server 


key = ""
secret = ""

with open('../scripts/api-key', "r") as f: 
	key = f.readline().rstrip()
	secret = f.readline().rstrip()

base_url = 'https://rogers.onshape.com'

client = Client(configuration={"base_url": base_url, "access_key": key, "secret_key": secret})

element = OnshapeElement(
        "https://rogers.onshape.com/documents/b7c65d78bde731408815188e/w/09daa8ec5418b4d1e583d4b3/e/fbca3f5c681a7618c9d7d895"
    )

sweep_cube = 'https://rogers.onshape.com/documents/aec16876714d70a447e5b140/w/c96b1b15861efbe1cf7dd9be/e/5f5788dd8bef0635f2776ac5'
normal = 'b7c65d78bde731408815188e/w/09daa8ec5418b4d1e583d4b3/e/fbca3f5c681a7618c9d7d895'

headers = {'Content-Type': 'application/json', 'Accept': 'application/vnd.onshape.v1+json'}
r = client.api_client.request(method='GET', url = base_url + '/api/partstudios/d/b7c65d78bde731408815188e/w/09daa8ec5418b4d1e583d4b3/e/fbca3f5c681a7618c9d7d895/features', query_params = {}, headers = headers)
# print(json.dumps(json.loads(r.data), indent=4))


# Parse the feature tree by looking at known keywords and removing unwanted params

whitelist = ['type', 'typeName', 'message', 'queries', 'parameterId', 'enumName', 'value',
			 'units', 'expression', 'constraints', 'features', 'featureType', 'featureId', 'name']

blacklist = ['hasUserCode', 'nodeId', 'namespace', 'suppressed']

translation = {'parameterId': 'parameter_id', }
# bt_type won't be hard 

# initial_grab = json.dumps(json.loads(r.data), indent=4)
initial_grab = json.loads(r.data)
# print(json.dumps(r.data, indent=4))

# Probably need just sketch data and feature data 

sketch_data = []
feature_data = []
misc_data = []
features_list = initial_grab['features']
# for item in features_list:     # for each feature in the list 
# 	type_num = item['type']
# 	typename = item['typeName']
# 	print('%s%s' % (typename, type_num))     # grab typename and number
# 	if typename == 'BTMSketch':
# 		# dont forget the typename of the sketch 
# 		entities = item['message']['entities']
# 		for i in entities: 
# 			type_num_ent = i['type']
# 			typename_ent = i['typeName']
# 			print(i)
# 			print('%s%s' % (typename_ent, type_num_ent))
# 			try: 
# 				message = i['message']
# 				if message['typeName'] == 'BTMSketchCurveSegment'


# 			except: 



# find all typenames, their types, and their messages 

features = {}

for i,item in enumerate(features_list):
	type_num = item['type']
	typename = item['typeName']
	btm_feature = '%s%s' % (typename, type_num)
	message = item['message']
	message['bt__type'] = btm_feature
	features.update({i: message})

# print(json.dumps(features, indent=4))

# This grabs all the necessary features we need to recreate a part

# for each part, create a function that can repopulate the feature tree 

# SKETCH CURVE SEGMENT 155
# start_point_id=f"LINE1.start",
# end_point_id=f"LINE1.end",
# start_param=0.0,
# end_param=1.0,
# geometry=line_geometry1,
# entity_id='LINE1',
# bt_type="BTMSketchCurveSegment-155",
all_functions = {}

sketch_curve_segment_trans = {'startPointId': 'start_point_id',
							  'endPointId': 'end_point_id', 
							  'startParam': 'start_param',
							  'endParam': 'end_param',
							  'geometry': 'geometry',
							  'entityId': 'entity_id',
							 }

line_geometry_trans = {'pntX': 'pnt_x', 'pntY': 'pnt_y', 'dirX': 'dir_x', 'dirY': 'dir_y'}

constraint_trans = {'constraintType': 'constraint_type', 'entityId': 'entity_id', }

param_string_trans = {'value': 'value', 'parameterId': 'parameter_id'}

param_quantity_trans = {'expression': 'expression', 'parameterId': 'parameter_id'}

param_enum_trans = {'enumName': 'enum_name', 'parameterId': 'parameter_id', 'value': 'value'}

circle_sketch_trans = {'radius': 'radius', 'xCenter': 'x_center', 'yCenter': 'y_center', 'xDir': 'x_dir', 'yDir': 'y_dir', 'clockwise': 'clockwise'}

sketch_curve_trans = {'centerId': 'center_id', 'entityId': 'entity_id'}

    # circle = BTMSketchCurve4(center_id=f"{CIRCLE_ID}.center", entity_id=CIRCLE_ID, geometry=circle_geometry)
# circle_geometry = BTCurveGeometryCircle115(radius=0.00635, xcenter=0.0127, ycenter=0.0127, xdir=.0127, ydir=0.0, clockwise=False)
# operation_domain = BTMParameterEnum145(
#     value="MODEL",
#     enum_name="OperationDomain",
#     parameter_id="domain",
# ) 
# length = BTMParameterQuantity147(expression="1*in", parameter_id="length")
# line_geometry4 = BTCurveGeometryLine117(
#         pnt_x=.0254, pnt_y=0.0, dir_x=-.0254, dir_y=0.0, bt_type="BTCurveGeometryLine-117"
# )

# point_string_param3 = BTMParameterString149(
#         value='point3', parameter_id="localFirst", bt_type="BTMParameterString-149"
#     )


# coincident_constraint1 = BTMSketchConstraint2(
#         constraint_type="COINCIDENT",
#         parameters=[point_string_param, line_end_string_param],
#         entity_id="constrainId",
#         bt_type="BTMSketchConstraint-2",
#     )
# line_end_string_param = BTMParameterString149(
#         value=f"'LINE1.start",
#         parameter_id="localSecond",
#         bt_type="BTMParameterString-149",
#     )

# feature_definition = BTFeatureDefinitionCall1406(feature=sketch)
#     client.part_studios_api.add_part_studio_feature(
#         did=part_studio.did,
#         wvm=part_studio.wvm,
#         wvmid=part_studio.wvmid,
#         eid=part_studio.eid,
#         bt_feature_definition_call_1406=feature_definition,
#         _preload_content=False,
#     )


# abstract these for loops into functions for ease of use, figure out the parameters 

for item in features:
	functions = []
	curr = features[item]

	if curr['bt__type'] == 'BTMSketch151': 
		# BTMSketchCurveSegment-155, BTCurveGeometryLine-117, BTMSketchConstraint-2,
		# BTMParameterString-149, BTMParameterQueryList-148, BTMIndividualQuery-138,
		# BTMParameterQuantity-147
		entities = curr['entities']
		constraints = curr['constraints']
		featureType = curr['featureType']
		name_sketch = curr['name']
		parameters = curr['parameters']
		entities_list = []
		for entity in entities: 
			bt_feature = '%s-%s' % (entity['typeName'], entity['type'])
			func_temp = {}
			if 'BTMSketchCurveSegment' in bt_feature:
				message = entity['message']
				for query in message: 
					try:
						translated = sketch_curve_segment_trans[query]
					except KeyError: 
						continue 
					if translated == 'geometry':
						bt_type = '%s-%s' % (message[translated]['typeName'], message[translated]['type']) 
						pnts = {}
						for pnt in message[translated]['message']:
							translated_pnt = line_geometry_trans[pnt]
							pnts.update({translated_pnt: message[translated]['message'][pnt]})
						pnts.update({'bt_type': bt_type})
						func_temp.update({'geometry': pnts })
					else:
						func_temp.update({translated: message[query]})
				func_temp.update({'bt_type': bt_feature})
				entities_list.append(func_temp)

			elif 'BTMSketchCurve' in bt_feature: 
				geometry = entity['message']['geometry']
				geometry_type = '%s%s' % (geometry['typeName'], geometry['type'])
				geos = {}
				ids = {}
				for mess in geometry['message']:
					translated = circle_sketch_trans[mess]
					geos.update({translated: geometry['message'][mess]})
				for i in entity['message']: 
					try: 
						translated = sketch_curve_trans[i]
					except KeyError: 
						continue 
					ids.update({translated: entity['message'][i]})
				entities_list.append({'geometry': geos, 'ids': ids, 'bt_type': geometry_type})
				functions.append({'entities': entities_list, 'bt_type': btm_feature})

		constraints_list = []
		for constraint in constraints:
			bt_feature = '%s-%s' % (constraint['typeName'], constraint['type'])
			func_temp = {}
			if 'BTMSketchConstraint' in bt_feature:
				message = constraint['message']
				for query in message: 
					temp_query = []
					if query == 'parameters': 
						for param in message[query]:
							temp = {}
							bt_type = '%s-%s' % (param['typeName'], param['type'])
							if 'BTMParameterString' in bt_type:
								for i in param['message']:
									try:
										translated_param = param_string_trans[i]
									except KeyError:
										continue
									temp.update({translated_param: param['message'][i]})
							elif 'BTMParameterQuantity' in bt_type: 
								for i in param['message']:
									try:
										translated_param = param_quantity_trans[i]
									except KeyError:
										continue
									temp.update({translated_param: param['message'][i]})
							temp.update({'bt_type': bt_type})
							temp_query.append(temp)
						func_temp.update({'constraints': temp_query})
					else:
						try: 
							translated = constraint_trans[query]
						except KeyError:
							continue
						func_temp.update({translated: message[query]})
				func_temp.update({'bt_type': bt_feature})
				constraints_list.append(func_temp)

		params_list = []
		for param in parameters:
			func_temp = {}
			param_bt_type = '%s-%s' % (param['typeName'], param['type'])
			if 'QueryList' in param_bt_type:
				queries = param['message']['queries']
				temp = []
				for query in queries:
					query_bt_type = '%s%s' % (query['typeName'], query['type'])
					if 'IndividualQuery' in query_bt_type:
						deterministic_ids = query['message']['geometryIds']
						parameter_id = param['message']['parameterId']
						temp.append({'deterministic_ids': deterministic_ids, 'parameter_id': parameter_id, 'bt_type': query_bt_type})
				func_temp.update({param_bt_type: temp})
				params_list.append(func_temp)
			elif 'ParameterQuantity' in param_bt_type:
				temp = {}
				for i in param['message']:
					try:
						translated_param = param_quantity_trans[i]
					except KeyError:
						continue
					temp.update({translated_param: param['message'][i]})
				func_temp.update({param_bt_type: temp})
				params_list.append(func_temp)
		all_functions.update({item: {'parameters': params_list, 'name': name_sketch, 'bt_type': 'BTMSketch151', 'entities': entities_list, 'constraints': constraints_list}})

	elif curr['bt__type'] == 'BTMFeature134':
		# enums, querylist, and quantity 
		name = curr['name']
		feature_type = curr['featureType']
		params_list = []
		for i, param in enumerate(curr['parameters']): 
			func_temp = {}
			bt_type = '%s-%s' % (param['typeName'], param['type'])
			if 'ParameterEnum' in bt_type:
				for i in param['message']:
					try:
						translated_param = param_enum_trans[i]
					except KeyError:
						continue
					func_temp.update({translated_param: param['message'][i]})
				params_list.append({bt_type: func_temp})
			elif 'QueryList' in bt_type: 
				queries = param['message']['queries']
				temp = []
				if len(queries) == 0: 
					parameter_id = param['message']['parameterId']
					temp.append({'parameter_id': parameter_id})
				else: 
					for query in queries:
						query_bt_type = '%s%s' % (query['typeName'], query['type'])
						if 'IndividualQuery' in query_bt_type:
							deterministic_ids = query['message']['geometryIds']
							parameter_id = param['message']['parameterId']
							temp.append({'deterministic_ids': deterministic_ids, 'parameter_id': parameter_id, 'bt_type': query_bt_type})
				func_temp.update({bt_type: temp})
				params_list.append(func_temp)
			elif 'ParameterQuantity' in bt_type: 
				temp = {}
				for i in param['message']:
					try:
						translated_param = param_quantity_trans[i]
					except KeyError:
						continue
					temp.update({translated_param: param['message'][i]})
				func_temp.update({bt_type: temp})
				params_list.append(func_temp)
		all_functions.update({item: {'feature_type': feature_type, 'name': name, 'parameters': params_list, 'bt_type': 'BTMFeature-134'} })


print(json.dumps(all_functions,indent=4))
# sketch = BTMSketch151(
#     entities=[line, line2, line3, line4],
#     name="Square",
#     parameters=[plane_query, length],
#     constraints=[coincident_constraint1, coincident_constraint2],
#     bt_type="BTMSketch-151",
# )
# length = BTMParameterQuantity147(expression="1*in", parameter_id="length")
# line_geometry4 = BTCurveGeometryLine117(
#         pnt_x=.0254, pnt_y=0.0, dir_x=-.0254, dir_y=0.0, bt_type="BTCurveGeometryLine-117"
# )
# coincident_constraint1 = BTMSketchConstraint2(
#         constraint_type="COINCIDENT",
#         parameters=[point_string_param, line_end_string_param],
#         entity_id="constrainId",
#         bt_type="BTMSketchConstraint-2",
#     )
# line_end_string_param = BTMParameterString149(
#         value=f"'LINE1.start",
#         parameter_id="localSecond",
#         bt_type="BTMParameterString-149",
#     )
# line = BTMSketchCurveSegment155(
#     start_point_id=f"LINE1.start",
#     end_point_id=f"LINE1.end",
#     start_param=0.0,
#     end_param=1.0,
#     geometry=line_geometry1,
#     entity_id='LINE1',
#     bt_type="BTMSketchCurveSegment-155",
# )
print('\nThe following functions will be created:\n')
for func in all_functions:
	func_dict = all_functions[func] 
	name = func_dict['name'].replace(' ', '_') + str(func)
	print('\t' + name)
	if func_dict['bt_type'] == 'BTMSketch151': 
		# create entities
		entities = func_dict['entities']
		entities_funcs = []

		for ent in entities: 
			if ent['bt_type'] == 'BTMSketchCurveSegment-155':
				func_string = "BTMSketchCurveSegment155(start_point=%s, end-point_id=%s, start_param=%s, end_param=%s, geometry=%s, entity_id=%s, bt_type=%s" % ()
				


			elif ent['bt_type'] == 'BTCurveGeometryCircle115':

	elif fun_dict['bt_type'] == 'BTMFeature-134'
		








# features --> message  --> entities
# 			   type
# 			   typename --> 

# features --> constraints

# features and sketches come afterwards 

# Hopefully we get a good enough dataset from just 3,4 examples of different functions
# Onshape JSONs definitely have to have a pattern of creation. 

# End Result: deserializing of OnShape PartStudio data (JSON) by feature element in the tree.
# 			  Create a Python file filled with functions that can iterate and remake the 
# 		      part piece by piece, and also describe metadata. 

# Takes in different part studio URLS and parses the Part. 

# Locate items based on the parent key

# organize into client functions 

# find parameters and fill variables with respective item_name

# discover formats that work, formats that don't work, report back 

# Try and formulate the necessary request to recreate the part for testing purposes 

# 

# parse through dictionary and categorize by listed terms, starting at parent 
# for value in initial_grab.values():
# 	if isinstance(value, list): 
# 		# check size of dictionary
# 		length_of_value_list = len(value)

# 		# iterate through list and find dictionaries
# 		for item in value: 
# 			if isinstance(item, dict):




# strip down more useless info and save data in onshape_client format 



# organize data and output as python function 

