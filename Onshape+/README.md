# Onshape scripts and tools

Here you can find resources on the Onshape API, Featurescripts, and other tests. Click on a link in the Table of Contents to navigate to the respective page.

## Table of Contents 
- [Contours](https://github.com/drybell/CEEO2020/tree/master/Onshape%2B/contour-onshape) contains standalone python scripts that converts an image to an Onshape sketch
- [EV3 to Onshape](https://github.com/drybell/CEEO2020/tree/master/Onshape%2B/ev3-onshape) Contains a tutorial that allows users to install the Onshape API python library on their EV3
- [Featurescipt VS Code Extension](https://github.com/drybell/CEEO2020/tree/master/Onshape%2B/featurescript) a failed attempt at creating a featurescript syntax highlighter for VS Code (need more time)
- [Featurescripts](https://github.com/drybell/CEEO2020/tree/master/Onshape%2B/fs_scripts) Some test featurescripts for API calls
- [JSONs](https://github.com/drybell/CEEO2020/tree/master/Onshape%2B/json_files) sample JSONs containing info on feature trees of Part Studios
- [Scripts](https://github.com/drybell/CEEO2020/tree/master/Onshape%2B/scripts) A vast collection of random scripts written to utilize Onshape API. More info inside.
- [Tests](https://github.com/drybell/CEEO2020/tree/master/Onshape%2B/tests) Test scripts and Feature Tree JSONs used when recreating feature trees in an Onshape Part Studio


# Old README notes from the beginning of the summer
 
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