import requests
import argparse 
from onshape_client.client import Client
import json 

## Needed to do pip3 install urllib3==1.25.9


### Adding small command-line tools 
parser = argparse.ArgumentParser(description='Test script for Onshape API')

parser.add_argument('-d', dest="did2", help="Specify a document id for your Onshape workspace")
parser.add_argument('-w', dest="wid2", help="Specify a workspace id for your Onshape workspace")

args = parser.parse_args()
### Still under construction 

key = ""
secret = ""

with open("api-key", "r") as f: 
	key = f.readline().rstrip()
	secret = f.readline().rstrip()

# print(key + " " + secret)

base_url = 'https://rogers.onshape.com'

document_id = '2696c6465ac59aff8ca3dfc1'

wid = 'be80594917e5b1877e38d94e'

part_studio_eid = 'bd2b08bfd9046a3e25896bf3'

# Let's try to create a part studio 

## I guess requests won't work, you'll have to use the onshape github
# def CreatePartStudio(base_url, document_id, wid, studio_name):
# 	urlparams = base_url + 'api/partstudios/d/' + document_id + wid
# 	print("Sending to: " + urlparams)

# 	r = requests.post(urlparams, headers=headers, json=body)
# 	return r

# r = CreatePartStudio(base_url, document_id, wid, "Testing!")

client = Client(configuration={"base_url": base_url, "access_key": key, "secret_key": secret})
# print(client.configuration.get_api_key_with_prefix("ACCESS_KEY"))

# client = Client

# url for get metadata
# tester = '/api/metadata/d/2696c6465ac59aff8ca3dfc1/w/be80594917e5b1877e38d94e/e/bd2b08bfd9046a3e25896bf3?depth=5&detailLevel=5&noNull=false&thumbnail=false&p-offset=0'



# Get Feature List: /assemblies/d/:did/w/wid/e/eid/features

# Create a new part studio given document and element id 
studio_name = "DOWN"
headers = {'Accept': 'application/vnd.onshape.v1+json', 'Content-Type': 'application/json'}
# body = {"name": studio_name}
# query = {"did": document_id, "wid": wid}
# r2 = client.api_client.call_api()
# r1 = client.api_client.request('GET', base_url + tester, headers=headers)
# print(r1)
# print(headers)
r = client.api_client.request('GET', url= base_url + '/api/assemblies/d/2696c6465ac59aff8ca3dfc1/w/be80594917e5b1877e38d94e/e/813c2254236b056011fdcba1/features', query_params={}, headers=headers, _preload_content=False)
# print(r.data)
x = json.loads(r.data)
print(x)


