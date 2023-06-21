#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key not in a_dictionary:
        return a_dictionary
    else:
        new_dict = {}
        for ki, val in a_dictionary.items():
            if ki != key:
                new_dict[ki] = val
        return new_dict
