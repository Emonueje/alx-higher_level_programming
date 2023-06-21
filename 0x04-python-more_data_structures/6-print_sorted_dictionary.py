#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_dict = {key: a_dictionary[key] for key in sorted(a_dictionary)}
    for i, j in sort_dict.items():
        print("{}: {}".format(i, j))
