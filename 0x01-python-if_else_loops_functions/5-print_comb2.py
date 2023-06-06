#!/usr/bin/python3
n = 0
for number in range(0, 100):
    if number == 99:
        print(number)
    elif number < n + 10 and number > n:
        print("{}{},".format(int(n / 10), number % 10), end=" ")
    if number == n + 10:
        n += 10
