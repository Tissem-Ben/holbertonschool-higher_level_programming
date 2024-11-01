#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    result = 0
    index = 1

    while index < len(argv):
        result += int(argv[index])
        index += 1

    print("{}".format(result))
