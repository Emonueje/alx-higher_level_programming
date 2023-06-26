#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    number_printed = 0
    i = 0
    while (i < x):
        try:
            print(my_list[i], end='')
            number_printed += 1
        except as e:
            break
        i += 1
    print()

    return number_printed
