import sys


from random import randint


def main():
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        n = int(sys.argv[2])
        file = open(filename, "w")
        for i in range(1,n+1):
            file.write(str(randint(1, 1000)))
            if i != n:
                file.write(str(" "))
        file.close()
    else:
        return "Please enter an argument"

if __name__ == '__main__':
    print(main())
