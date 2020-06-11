# This script will take the json returned from getting feature_studio contents and will output a
# formatted featurescript file
import argparse 

parser = argparse.ArgumentParser(description='Takes in a valid response body from an Onshape Get Feature Contents')

parser.add_argument('-i', dest="input_file", help="An input json file to read")
parser.add_argument('-o', dest="output_file", help="An output .fs file to write to")

args = parser.parse_args()

if (not (args.input_file and args.output_file)):
    print("ERROR: You must specify an input and output file for parsing...")
elif ".json" not in args.input_file: 
    print("ERROR: Input file must have a .json extension")
elif ".fs" not in args.output_file: 
    print("ERROR: Output file must have a .fs extension")
else: 
    with open(args.input_file,"r") as json_data:
        json_data.readline()
        contents = json_data.readline()
        contents = contents[16:]
        contents = contents[:-2]
        contents = contents[1:-1]
        # with open("test.fs", "w") as f: 
        contents = contents.replace("\\\\", "\\")
        contents = contents.replace("\\n", "\n")
        contents = contents.replace("\\\"", "\"")
        with open(args.output_file, "w") as f: 
            f.write(contents)


