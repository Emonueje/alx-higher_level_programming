#!/usr/bin/python3
def best_score(a_dictionary):
    bestscore = 0
    if a_dictionary is None:
        return  None
    for key in a_dictionary:
        if a_dictionary.get(key) > bestscore:
            bestscore = a_dictionary.get(key)
    for ki in a_dictionary:
        if a_dictionary.get(ki) == bestscore:
            return ki
    return None
