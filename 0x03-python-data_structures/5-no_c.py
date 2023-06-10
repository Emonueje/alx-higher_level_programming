#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return None
    new_string_list = list(my_string)
    for i in range(len(new_string_list)):
        if new_string_list[i] in "cC":
            new_string_list[i] = ''
    new_string = ''.join(new_string_list)
    return new_string
