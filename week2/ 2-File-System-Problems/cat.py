import sys

def cat():
	if len(sys.argv) > 1:
		filename = sys.argv[1]
		file = open (filename, "r")
		content = file.read()
		return content
		file.close()
	else:
		return "Please enter a file"

if __name__ == '__cat__':
	print(cat())
