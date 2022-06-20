#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    int_only = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            int_only += 1
        except (ValueError, TypeError):
            continue
        print("")
        return int_only
