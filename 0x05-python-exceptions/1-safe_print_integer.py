#!/usr/bin/python3
""" checks the type of value passed in """


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        ret_type = True
    except Exception:
        ret_type = False
    return (ret_type)
