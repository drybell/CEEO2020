# Assuming json file is indented 4 spaces and is used in conjunction with our 
# scripts
def fs_parser(input_data, output):
    if ".json" not in input_data: 
        print("Input file must have .json extension")
    elif ".fs" not in output: 
        print("Output file must have .fs extension")
    else:
        with open(input_data,"r") as data: 
            data.readline()
            contents = data.readline()
            contents = contents[16:]
            contents = contents[:-2]
            contents = contents[1:-1]
            contents = contents.replace("\\\\", "\\")
            contents = contents.replace("\\n", "\n")
            contents = contents.replace("\\\"", "\"")
            with open(output, "w") as f: 
                f.write(contents) 
            print("Created new FeatureScript file: %s" % (output))

