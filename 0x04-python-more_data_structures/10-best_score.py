#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None or len(a_dictionary) == 0::
        return None
    else:
        for key, value in a_dictionary.items():
            if max(a_dictionary.values()) == value:
                return key
