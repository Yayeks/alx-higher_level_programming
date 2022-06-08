#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if type(key) == type('str'):
        a_dictionary[key] = value
    for k in a_dictionary.keys():
        if type(k) != type('str'):
            return None
        break
    return (a_dictionary)
