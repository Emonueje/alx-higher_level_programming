#!/usr/bin/python3
def update_dictionary(a_dicitionary, key, value):
    for x, y in a_dictionary.items():
        if x is key:
            y = value
    a_dictionary[key] = value
    return a_dictionary
