import sys


from random import randint


def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        file = open(filename, "r")
        content = file.read()
        #result = [int(i) for i in content.split()]
        result = map(int, content.split())
        return sum(result)
        file.close()
    else:
        return "Please enter an argument"

if __name__ == '__main__':
    print(main())
