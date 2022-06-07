#!/usr/bin/python3
import sys


def main():
    arguments = sys.argv
    sum = 0
    for i in range(1, len(arguments)):
        sum += int(arguments[i])
    print("{}".format(sum))


if __name__ == "__main__":
    main()
