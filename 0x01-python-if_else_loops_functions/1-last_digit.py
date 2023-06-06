#!/usr/bin/python3
#import random
#number = random.randint(-10000, 10000)
#if number < 0:
#   n = -(-number % 10)
#   if n < 6 and n != 0:
#       print(f"Last digit of {number} is {n} and is less than 6 and not 0")
#else:
#   n = number % 10
#   if n > 5:
#       print(f"Last digit of {number} is {n} and is greater than 5")
#   elif n == 0:
#       print(f"Last digit of {number} is {n} and is 0")
#   else:
#        print(f"Last digit of {number} is {n} an is less than 6 and not 0")
import random
number = random.randint(-10000, 10000)
if number < 0:
    new_number = -1 * number
    last_digit = -1 * (new_number % 10)
else:
    new_number = number
    last_digit = new_number % 10
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit < 6 and last_digit != 0:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
