#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    type(key)
    if key not in a_dictionary:
        return a_dictionary
    else:
        new_dict = {}
        for ki, val in a_dictionary.items():
            if ki is key:
                continue;
            else:
                new_dict[ki] = val
        return new_dict
