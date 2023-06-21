#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for ki, val in a_dictionary.items():
        new_dict[ki] = val *2
    return new_dict
