# Onshape Python API 
Beta version of utilizing the Onshape API Explorer as a command-line tool 

## How to Use: 
Clone this directory, add a file called `api-key`, on the first line add your Onshape key, add a newline, then add your secret. Modify `shapeapi.py` if you're not using the default base_url 
`rogers.onshape.com`

Save the file, then run: 

`python3 shapeapi.py -d your-did-here -w your-wid-here -e your-eid-here`

Need Help? 
`python3 shapeapi.py -h`

## What is the did, wid, and eid? 
(Will add images and explanations later)

## Update: June 11th
We are currently working on VSCode support for syntax-highlighting of FeatureScript code (.fs files)! If you are interested, look within the featurescript folder. 

## Added parse_featurecontents_json.py to parse FeatureScript contents returned from Onshape API 

### Usability: 
`python3 parse_featurecontents_json.py -i input_file.json -o output_file.fs` 

**NOTE1**: Input files must be relative paths to the location of the json file and MUST have a `.json` file extension. 
Example Snippet: `-i json/my-file.json` 
**NOTE2**: Output files must have a `.fs` file extension

### Data Pipeline for FeatureScripts High Level Overview:
We are trying to start off with a local FeatureScript, then calling a script that can output the .stl file for running the respective FeatureScript