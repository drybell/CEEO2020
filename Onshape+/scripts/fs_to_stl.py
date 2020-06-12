# This script will take in a .fs file and return with a newly created document,
# part studio, feature studio, and execute the featurescript to create a part, 
# as well as providing the link to download the .stl file for the part 

from onshape_client import Client
import json
# WHICH API CALLS ARE NEEDED? 
# Create Document /api/documents/                                       --> get document id 
# Create Workspace /api/documents/did/workspaces/wid/copy               --> get workspace id 
# Create Feature Studio /api/featurestudios/d/did/w/wid                 --> get feature id or something of the sort 
# Update Feature Studio Contents /api/featurestudios/d/did/w/wid/e/eid  --> update the featurestudio with fs code 
# I GUESS WE STILL MAKE THE FEATURE STUDIO FOR LATER USE BUT EVALUATE FEATURESCRIPT? 
# EVALUATE FEATURESCRIPT --> will output us a message and the resulting  as well 
# Add Feature --> Using object data given from evaluate featurescript 
# Export Part Studio to STL 

# API URLS IN ORDER 
# /api/documents/                                                                     DOCUMENT 
# /api/documents/did/workspaces/wid/copy                                              WORKSPACE 
# /api/featurestudios/d/did/w/wid                                                     FEATURE STUDIO
# /api/featurestudios/d/did/w/wid/e/eid                                               UPDATE FEATURE STUDIO CONTENTS
# /api/partstudios/d/did/w/wid/e/eid/featurescript                                    EVALUATE FEATURESCRIPT 
# /api/partstudios/d/did/w/wid/e/eid/stl?grouping=true&scale=1.0&units=inch&mode=text PART STUDIO TO STL 
DOCUMENTNAME = 'TEST'
FEATURESCRIPT = 'test.fs'

key = ""
secret = ""

with open("api-key", "r") as f: 
	key = f.readline().rstrip()
	secret = f.readline().rstrip()

base_url = 'https://rogers.onshape.com'

def printables(response):
    print("Headers: ", end="")
    print(response.getheaders())
    print()
    print("Body Details: ", end="")
    x = json.loads(response.data)
    print(json.dumps(x, indent=4))

client = Client(configuration={"base_url": base_url, "access_key": key, "secret_key": secret})
headers = {'Accept': 'application/vnd.onshape.v1+json', 'Content-Type': 'application/json'}

# SIMPLIFIED RUN: CREATE DOCUMENT, EVALUATE FEATURESCRIPT 
# Create a Document 
payload = {'isPublic': 'false', 'name': DOCUMENTNAME}
response = client.api_client.request('POST', url=base_url + '/api/documents/', query_params={}, body=payload)
printables(response)
# WHAT INFO DO WE GRAB FROM HERE FOR IT TO WORK? 
 
data = ""
with open(FEATURESCRIPT, "r") as f: 
    total = f.readlines()
    for line in total: 
        data += line