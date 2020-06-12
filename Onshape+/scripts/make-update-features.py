from onshape_client.client import Client
import json 

key = ""
secret = ""

with open("api-key", "r") as f: 
	key = f.readline().rstrip()
	secret = f.readline().rstrip()

base_url = 'https://rogers.onshape.com'