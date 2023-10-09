#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    num = -number
    last_number = num % 10
    last_number = -last_number
else:
    num = number
    last_number = num % 10
print(f"Last digit of {number:d}",end=" ")
if last_number > 5:
    print(f"is {last_number:d} and is greater than 5")
elif last_number == 0:
    print(f"is {last_number:d} and is 0")
elif last_number < 6 and last_number != 0:
    print(f"is {last_number:d} and is  less than 6 and not 0")
