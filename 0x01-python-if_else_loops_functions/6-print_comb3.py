#!/usr/bin/python3
for num in range(0, 10):
    for n in range(num + 1, 10):
        if (num != 8 or n != 9):
            print("{}{},".format(num, n), end=" ")
        else:
            print("{}{}".format(num, n))
