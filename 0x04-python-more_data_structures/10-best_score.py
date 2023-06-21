#!/usr/bin/python3
def best_score(a_dictionary):
    best_score = 0
    if a_dictionary is None:
        return None
    for key in a_dictionary:
        if a_dictionary.get(key) > best_score:
            best_score = a_dictionary.get(key)
    for ki in a_dictionary:
        if a_dictionary.get(ki) == best_score:
            return ki
    return None
