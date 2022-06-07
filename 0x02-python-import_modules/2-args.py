#!/usr/bin/python3
import sys


def ags():
    number = len(sys.argv) - 1
    if number == 0:
        print("0 arguments.")
    elif number == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{:d} arguments:".format(number))
        for i in range(1, number + 1):
            print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    ags()
