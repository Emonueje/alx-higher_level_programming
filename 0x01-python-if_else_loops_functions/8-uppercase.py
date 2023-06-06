#!/usr/bin/python3
def islower(c):
    if ord(c) in range(ord('a'), ord('z') + 1):
        return True
    else:
        return False

def to_upper(c):
    if islower(c):
        return chr(ord(c) - 32)
    return c


def uppercase(str):
    for c in str:
        print("{}".format(to_upper(c)), end="")
    print()
