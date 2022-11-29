#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    remainder = number % -10
else:
    remainder = number % 10
if remainder > 5:
    flag = "and is greater than 5"
elif remainder == 0:
    flag = "and is 0"
elif remainder < 6 and remainder != 0:
    flag = "and is less than 6 and not 0"
print(f"Last digit of {number} is {remainder} {flag}")
