#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 1

    args = sys.argv[1:]
    num_args = len(args)

    if num_args == 1:
        print("{} argument:".format(1))
        print("{}: {}".format(1, args[0]))
    elif num_args == 0:
        print("{} arguments.".format(0))
    elif num_args > 1:
        print("{} arguments:".format(num_args))
        for arg in args:
            print("{}: {}".format(i, arg))
            i += 1
