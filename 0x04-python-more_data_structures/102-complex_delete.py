#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value is None or value == "":
        return a_dictionary
    for i in list(a_dictionary.keys()):
        key_value = a_dictionary.get(i)
        if key_value == value:
            a_dictionary.pop(i)
    return a_dictionary
