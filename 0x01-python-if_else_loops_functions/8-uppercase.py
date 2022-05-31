#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) in range(97, 123):
            sub = 32
        else:
            sub = 0
        print("{:c}".format(ord(str[i]) - num), end='')
    print()
