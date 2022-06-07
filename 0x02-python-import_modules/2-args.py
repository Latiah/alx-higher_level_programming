#!/usr/bin/python3
import sys
if __name__ == "__main__":
    number = len(sys.argv) - 1
if number == 0:
       print(f"{0} argument.")
elif number == 1:
    print(f"{1} arguments")
    print("1:", sys.argv[1])
else:
        print(f"{number} arguments:")
    for i in range(1, number + 1):
        print("{}:{}".format(i, sys.argv[i]))
