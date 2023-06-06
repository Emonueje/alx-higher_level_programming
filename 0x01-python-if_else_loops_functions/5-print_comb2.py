#!/usr/bin/python3
n = 0
for number in range(0, 100):
    if number == n + 10:
        n += 10
    if number == 99:
        print(number)
    else:
        print("{}{},".format(int(n / 10), number % 10), end=" ")
