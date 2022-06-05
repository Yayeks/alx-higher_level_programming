#!/usr/bin/python3
def no_c(my_string):
    new_string = [m for m in my_string if m != 'c' or m != 'C']
    return ("".join(new_string))
