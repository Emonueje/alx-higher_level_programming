#!/usr/bin/python3
for alphabt in range(ord('a'), ord('z') + 1):
    if alphabt == ord('e') or alphabt == ord('q'):
        continue
    else:
        print("{}".format(chr(alphabt)), end="")
