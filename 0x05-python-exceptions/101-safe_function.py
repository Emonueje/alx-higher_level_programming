#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        result = fct(*args)
    except Exception as ex:
        print("Exception: {:s}".format(str(ex)), file=stderr)
        return None
    else:
        return (result)
