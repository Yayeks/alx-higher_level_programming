#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    start = 0
    while start < x:
        try:
            print("{}".format(my_list[i]), end="")
            start += 1
        except IndexError:
            break
    print("")
    return start
