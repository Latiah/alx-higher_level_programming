#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if sys.argv[0]:
       print(f"{0} argument.")
    else:
        print(f"{len(sys.argv)} arguments:")
    for i, arg in enumerate(sys.argv):
        print(f"{i:>6}:{arg}")
