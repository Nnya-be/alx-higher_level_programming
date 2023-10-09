#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    num = -number
else:
    num = number
print(f"Last digit of {number:d}")
last_number = num % 10
if last_number > 5:
	print(f"is {last_number:d} and is greater than 5")
elif last_number == 0:
	print(f"is {last_number:d} and is 0")
elif last_number < 6 and last_number != 0:
	print(f"is {last_number:d} and is  less than 6 and not 0")

