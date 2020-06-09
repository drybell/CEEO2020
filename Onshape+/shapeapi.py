from onshape_client.client import Client
import argparse 

# Creating Feature Studio: /api/featurestudios/d/did/w/wid POST 
# Feature Studio Contents: /api/featurestudios/d/did/w/wid/e/eid GET 
# Feature Studio Specs: /api/featurestudios/d/did/w/wid/e/eid/featurespecs GET 
# Creating Part Studio: /api/partstudios/d/did/w/wid POST
# Create Part Studio Translation: /api/partstudios/d/did/w/wid/e/eid/translations POST 
# Add feature in Part Studio: /api/partstudios/d/did/w/wid/e/eid/features POST
# Part Studio Body Details: /api/partstudios/d/did/w/wid/e/eid/bodydetails GET
# Part Studio Delete Feature: /api/partstudios/d/did/w/wid/e/eid/features/featureid/fid DELETE
# Part Studio Update Feature: /api/partstudios/d/did/w/wid/e/eid/features/featureid/fid POST
# Parts Body Details: /api/parts/d/did/w/wid/e/eid/partid/pid/bodydetails GET
# Create Document: /api/documents POST
# Copy Workspace: /api/documents/did/workspaces/undefined/copy POST 
# Create Version: /api/documents/d/did/versions POST 
# Create Workspace: /api/documents/d/did/workspaces POST

### Parsing Arguments 
parser = argparse.ArgumentParser(description='Onshape API')

parser.add_argument('-d', dest="did", help="Specify a document id (did) for your Onshape workspace")
parser.add_argument('-w', dest="wid", help="Specify a workspace id (wid) for your Onshape workspace")
parser.add_argument('-e', dest="eid", help="Specify an element id (eid) for your Onshape workspace")

args = parser.parse_args()

flags = "OFF"

if (args.did and args.wid and (not args.eid)):
    print("You have specified only did and wid, so queries that need eid won't work...")
    flags = "NO_EID"
elif ((not args.did) or (not args.wid)):
    print("You need to specify both did and wid for this to work")
    exit()
else: 
    print("User specified\ndocument_id: %s\nworkspace_id: %s\nelement_id: %s" % (args.did, args.wid, args.eid))
    flags = "ALL"

### Finding a file named api-key within this directory and setting key and secret for setting up the client 
with open("api-key", "r") as f: 
	key = f.readline().rstrip()
	secret = f.readline().rstrip()

# MODIFY THIS IF YOU WANT cad.onshape.com, don't forget to modify key and secret as well
base_url = "https://rogers.onshape.com"

# Setting up the client
client = Client(configuration={"base_url": base_url, "access_key": key, "secret_key": secret})

# IF A QUERY REQUIRES AN FID OR A PID, DON'T FORGET TO ASK THE USER TO SUPPLY ONE 
with_eid = {'feature-studio-contents': ['GET', '/api/featurestudios/d/did/w/wid/e/eid'],
            'feature-studio-specs': ['GET', '/api/featurestudios/d/did/w/wid/e/eid/featurespecs'],
            'part-studio-translation': ['POST','/api/partstudios/d/did/w/wid/e/eid/translations'],
            'add-feature-part-studio': ['POST','/api/partstudios/d/did/w/wid/e/eid/features'],
            'part-studio-body-details': ['GET','/api/partstudios/d/did/w/wid/e/eid/bodydetails'],
            'part-studio-delete-feature': ['DELETE','/api/partstudios/d/did/w/wid/e/eid/features/featureid/fid'],
            'part-studio-update-feature': ['POST','/api/partstudios/d/did/w/wid/e/eid/features/featureid/fid'],
            'parts-body-details': ['GET','/api/parts/d/did/w/wid/e/eid/partid/pid/bodydetails'],
}

without_eid = {'create-feature-studio': ['POST', '/api/featurestudios/d/did/w/wid'],
               'create-part-studio': ['POST','/api/partstudios/d/did/w/wid'],
               'create-document': ['POST','/api/documents'],
               'copy-workspace': ['POST','/api/documents/did/workspaces/undefined/copy'],
               'create-version': ['POST','/api/documents/d/did/versions'],
               'create-workspace': ['POST','/api/documents/d/did/workspaces'],
}

if flags == "ALL":
    print("Using queries with wid, did, and eid specified...")
    print("NOTE! EARLY VERSION. Some queries require further info (like a feature id). Please have this handy")
    print("User query options are:")
    for key in with_eid: 
        print("%s: A %s call to %s" % (key, with_eid[key][0], with_eid[key][1]))
elif flags == "NO_EID":
    print("Using queries with no_eid specified...")
    for key in without_eid: 
        print("%s: A %s call to %s" % (key, without_eid[key][0], without_eid[key][1]))
else: 
    print("Something failed...")
    exit()








