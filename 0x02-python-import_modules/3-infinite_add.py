#!/usr/bin/python3
from sys import argv
num = len(argv) - 1
total = 0
for i in range(num):
    total += int(argv[i])
    print(total)
