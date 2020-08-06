# Onshape scripts

### Note: output_python_files
Contains feature tree JSONs and parsed JSONs that helped create the Feature Tree to Python translator

## Notable Scripts 
* [feature_tree_parser.py](https://github.com/drybell/CEEO2020/blob/master/Onshape%2B/scripts/feature_tree_parser.py): My brute force algorithm that translates a JSON feature Tree to a working Python function that can resend the features to another part studio. Further work will allow the creation of a button for our app that autopopulates a feature for a user who is stuck on an activity. 

* [script_version_parser.py](https://github.com/drybell/CEEO2020/blob/master/Onshape%2B/scripts/script_version_parser.py): CLI version of the above script, has four flags (-u, -o, -p, -a) explained below: 
    - **-u**: a valid URL for a Part Studio in Onshape
    - **-o**: an output (Python) file to write to
    - **-p**: path to your Onshape api key and secret file
    - **-a**: output URL for a different Part Studio in Onshape

**Example Usage:** 
```
$ python3 script_version_parser.py -p ../scripts/api-key -o testdemo.py -u https://rogers.onshape.com/documents/b7c65d78bde731408815188e/w/09daa8ec5418b4d1e583d4b3/e/96d39b57bfcc8cca0d96c2b5 -a https://rogers.onshape.com/documents/b7c65d78bde731408815188e/w/09daa8ec5418b4d1e583d4b3/e/cf9e349d44e4ac66367f48fe && python3 testdemo.py
```
This will take an input part studio, recreate each feature as a function, and output the necessary info to a python file named testdemo.py. testdemo.py will then be run, outputting the features to another part studio

* [generalapi.py](https://github.com/drybell/CEEO2020/blob/master/Onshape%2B/scripts/generalapi.py): My initial stab at creating a general API CLI tool for our CEEO PTC teams that allows ease of use and a simple getting started experience