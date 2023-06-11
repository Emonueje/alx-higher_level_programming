#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    if len(my_list) == 0:
        return None
    test = -9223372036854775808
    for i in my_list:
        if i > test:
            test = i
    return (test)
