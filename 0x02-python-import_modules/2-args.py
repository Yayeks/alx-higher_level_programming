#!/usr/bin/python3
if __name__ = "__main__":
    from sys import argv

    num = len(argv) - 1
    if num == 0:
        print("{} arguments.".format(num))
    else:
        if num == 1:
            print("{} argument:".format(num))
        else:
            print("{} arguments:".format(num))
        for i in range(num):
            print("{}: {}".format(i+1, argv[i+1]))
