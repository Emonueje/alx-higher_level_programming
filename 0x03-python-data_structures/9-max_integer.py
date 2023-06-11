#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    test = 0
    for i in my_list:
        if i > test:
            test = i
    return test
