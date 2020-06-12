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
parser.add_argument('-e', dest="eid", help="Specify an element id (eid) for your Onshape workspace (optional)")

args = parser.parse_args()

flags = "OFF"

if (args.did and args.wid and (not args.eid)):
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
headers = {'Accept': 'application/vnd.onshape.v1+json', 'Content-Type': 'application/json'}

# IF A QUERY REQUIRES AN FID OR A PID, DON'T FORGET TO ASK THE USER TO SUPPLY ONE 
# IF OPTIONAL, PREPEND opt- to the front of the string 
# IF BOOLEAN, PREPEND b- to the front of the string 
# IF NUMBER, PREPEND n- to the front of the string 
# If OBJECT, PREPEND O- to the front of the string
# CAN'T DO MICROVERSIONS AND VERSIONS YET.......
# GET CALLS DON'T HAVE REQUEST BODIES 
# EXPORT PART STUDIO AS STL 
with_eid = {'feature-studio-contents': [['GET', '/api/featurestudios/d/did/w/wid/e/eid'], []],
            'feature-studio-specs': [['GET', '/api/featurestudios/d/did/w/wid/e/eid/featurespecs'],[]],
            'part-studio-translation': [['POST','/api/partstudios/d/did/w/wid/e/eid/translations', 'configuration', 'formatName', 'includeExportIds', 'linkDocumentWorkspaceId', 'partIds', 'storeInDocument'],[]],
            'part-studio-add-feature': [['POST','/api/partstudios/d/did/w/wid/e/eid/features', 'O-feature', 'b-opt-rejectMicroversionSkew', 'serializationVersion', 'sourceMicroversion'],[]],
            'part-studio-body-details': [['GET','/api/partstudios/d/did/w/wid/e/eid/bodydetails', 'opt-configuration', 'opt-linkDocumentId', 'opt-rollbackBarIndex'],['opt-configuration', 'opt-linkDocumentId', 'n-opt-rollbackBarIndex']],
            'part-studio-delete-feature': [['DELETE','/api/partstudios/d/did/w/wid/e/eid/features/featureid/fid'],[]],
            'part-studio-update-feature': [['POST','/api/partstudios/d/did/w/wid/e/eid/features/featureid/fid', 'O-feature', 'O-feature.message', 'feature.type', 'feature.typeName', 'b-opt-rejectMicroversionSkew', 'serializationVersion', 'sourceMicroversion'], []],
            'parts-body-details': [['GET','/api/parts/d/did/w/wid/e/eid/partid/pid/bodydetails'], ['opt-configuration', 'opt-linkDocumentId']],
}

without_eid = {'create-feature-studio': ['POST', '/api/featurestudios/d/did/w/wid','name'],
               'create-part-studio': ['POST','/api/partstudios/d/did/w/wid','name'],
               'create-document': ['POST','/api/documents','b-isPublic','name','opt-ownerld','n-ownerType'],
               'copy-workspace': ['POST','/api/documents/did/workspaces/wid/copy','b-opt-isPublic','newName','opt-ownerld','opt-ownerTypeIndex'],
               'create-version': ['POST','/api/documents/d/did/versions','opt-description','documentId','b-opt-fromHistory','opt-microversionId','name','opt-workspaceId'],
               'create-workspace': ['POST','/api/documents/d/did/workspaces','opt-description','opt-microversionId','name','opt-versionId','opt-workspaceId'],
}

# Will change to a class later 

# New Design for adding request body JSON (JavaScript Object Notation)
# payload = {}
# for i in range(2,len(with_eid[key])):
#     info = input("Please specify %s for the request body: " % (with_eid[key][i]))
#     payload.update({with_eid[key][i]: info})

# request = client.api_client.request(method, url=url, headers=headers, body=payload)


def setQuery(available_queries):
    flag = False
    user_input = ""
    while (not flag): 
        user_input = input("Please type in a query (dashes included): ") 
        if user_input in available_queries: 
            print("User specified %s" % (user_input))
            flag = True 
    return user_input

response = None
if flags == "ALL":
    print("Using queries with wid, did, and eid specified...")
    print("NOTE! EARLY VERSION. Some queries require further info (like a feature id). Please have this handy")
    print("User query options are:")
    for key in with_eid: 
        print("%s: A %s call to %s" % (key, with_eid[key][0], with_eid[key][1]))
    print()
    query = setQuery(with_eid)
    payload = {}
    body_list = with_eid[query][0]
    string_flags = ['opt-', 'b-', 'n-', 'O-']
    # url_params = with_eid[query][1][1]
    if len(body_list) > 2:
        for i in range(2, len(body_list)):
            curr = body_list[i]
            # TODO: IF HYPHENS EXIST IN THE BEGINNING OF THE WORD, REMOVE THEM SO USER ISN'T CONFUSED
            opt = True 
            user = ""
            print("Current request body parameter: %s" % (curr))
            if 'opt-' in curr:
                user = input("This is an optional parameter, type in \'y\' or \'n\' if you want to use it: ")
                if user == "n":
                    opt = False 
            if 'b-' in curr and opt:
                # IF USER MESSES UP, WE DON'T WANT THE PROGRAM TO END, BUT FOR THEM TO TRY AGAIN 
                check = False
                while not check: 
                    user = input("This query is of type Boolean. Please type in \'true\' or \'false\': ")
                    if user == 'true' or user == 'false':
                        check = True
                    else: 
                        # user didn't type in true or false 
                        print('You have not entered \'true\' or \'false\'. Try again.')
            if 'n-' in curr and opt : 
                # usually is 0 or 1, could be different, but whatever. 
                check = False
                while not check: 
                    user = input("This query is of type Number. Please type in \'0\' or \'1\': ")
                    if user == '0' or '1':
                        check = True
                    else: 
                        # user didn't type in type Number (0 or 1) 
                        print('You have not entered \'0\' or \'1\'. Try again.')
            if 'O-' in curr and opt:   
                # need to read in some kind of .json file; will start off with having the user input .json file   
                # BROKEN, BUT IF A FEATURE IS NEEDED WE NEED TO TAKE IN SOMETHING THAT LOOKS LIKE A FEATURE JSON 
                # CHECK first lines of 1inchcube.json for guidance 
                check = False 
                content = []
                while not check: 
                    user = input("Please specify a relative file path (from the directory this script was run) to your .json file: ")
                    try 
                        with open(user, "r") as f: 
                            content = f.readlines()   
                        check = True
                    except Exception e: 
                        print("File not found, try again")
                user = parse_
            if not any([sub in curr for sub in string_flags]):
                user = input("Please specify %s: " % (curr))

            payload.update(curr: user)



    else:
        # print only if we don't have a complete query
        print("ERROR: This is not a valid request")

elif flags == "NO_EID":
    print("Using queries with no_eid specified...")
    for key in without_eid: 
        print("%s: A %s call to %s" % (key, without_eid[key][0], without_eid[key][1]))
    print()
    query = setQuery(without_eid)
    if query == 'create-document':
        # only functionality is isPublic and name 
        check = False
        isPublic = False
        name = ""
        while not check: 
            getPublic = input("Input t or f (true or false) for your document to be public: ")
            if getPublic == 'f' or getPublic == 't':
                if getPublic == 'f': 
                    isPublic = 'false'
                else: 
                    isPublic = 'true'
                name = input("Input a name for your document: ")
                check = True
        payload = {'isPublic': isPublic, 'name': name}
        response = client.api_client.request(without_eid[query][0], url=base_url + without_eid[query][1], query_params={}, body=payload)
        # Figure out a more readable solution 
        print(response.getheaders())
        exit()
    else: 
        # MOST OF THESE HAVE JUST DESCRIPTION AND NAME, CAN MAKE A FUNCTION TO DO THIS INSTEAD 
        method = without_eid[query][0]
        url = without_eid[query][1]
        if 'wid' not in url: 
            # create-version and create-workspace 
            fixed_url = url.replace('did', args.did)
            payload = {}
            if query == "create-version":
                # only description, document-id and name are functional 
                # TODO: microID and microversion
                description = input("Specify a description for your version: ")
                name = input("Specify a name for your version: ")
                payload = {'documentId': args.did, 'name': name, 'description': description}
            else: 
                # versionId = input("Specify a versionId:")
                description = input("Specify a description: ")
                name = input("Specify a name: ")
                payload = {'description': description, 'name': name}
            response = client.api_client.request(method, url=base_url + fixed_url, query_params={}, headers=headers, body=payload)
            print(response.getheaders())
            exit()
        elif query == 'create-feature-studio': 
            fixed_url = url.replace('did', args.did)
            fixed_url = fixed_url.replace('wid', args.wid)
            # print("Method: %s URL: %s" % (method, base_url + fixed_url))
            name = input("Specify a name for your feature studio: ")
            payload = {'name': name}
            response = client.api_client.request(method, url=base_url + fixed_url, query_params={}, headers=headers, body=payload)
            print(response.getheaders())
            exit()
        elif query == 'create-part-studio': 
            fixed_url = url.replace('did', args.did)
            fixed_url = fixed_url.replace('wid', args.wid)
            name = input("Specify a name for your part studio: ")
            payload = {'name': name}
            response = client.api_client.request(method, url=base_url + fixed_url, query_params={}, headers=headers, body=payload)
            print(response.getheaders())
            exit()
        else: 
            # copy workspace 
            fixed_url = url.replace('did', args.did)
            fixed_url = fixed_url.replace('wid', args.wid)
            name = input("Specify a new name for your workspace: ")
            payload = {'name': name}
            response = client.api_client.request(method, url=base_url + fixed_url, query_params={}, headers=headers, body=payload)
            print(response.getheaders())
            exit()

        
else: 
    print("Something failed...")
    exit()








