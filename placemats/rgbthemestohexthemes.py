import os
import argparse 
import json

# TODO: VISUALIZE THE COLOR THEMES (pygame?)

parser = argparse.ArgumentParser(description='Generate Hex Color Themes for creative use')
parser.add_argument('-n', dest="num", help="Number of themes to generate", default=1)

args = parser.parse_args()


# simple conversion, only works for up to 255 (don't want to build recursive case)
def convert_to_hex(color):
	switcher = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}

	fl = ""
	sl = ""
	firstletter = int(color / 16)
	secondletter = color % 16 

	if secondletter >= 10: 
		sl = switcher.get(secondletter)
	else: 
		sl = str(secondletter)
	if firstletter >= 10: 
		fl = switcher.get(firstletter)
	else: 
		fl = str(firstletter)

	return fl + sl

overall = []
for i in range(int(args.num)):
	theme = []
	stream = os.popen('curl -s \'http://colormind.io/api/\' --data-binary \'{"model":"default"}\'')
	output = stream.read()
	test = json.loads(output)
	array = test['result']
	for rgb in array: 
		string = ""
		for color in rgb:
			string += convert_to_hex(color)
		theme.append(string)
	overall.append(theme)

print("Themes are:")
for theme in overall:
	for color in theme: 
		print(color, end=" ")
	print()