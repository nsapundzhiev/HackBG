import sys

def main():
	if len(sys.argv) > 1:
		for i in range(1,len(sys.argv)):
			filename = sys.argv[i]
			file = open (filename, "r")
			content = file.read()
			print (content)
			file.close()
	else:
		return "Please enter a file"

if __name__ == '__main__':
	print(main())
