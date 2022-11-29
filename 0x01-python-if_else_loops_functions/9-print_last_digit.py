#!/bin/usr/python3
def print_last_digit(number):
    if number < 0:
        remainder = (number % -10)*-1
        print("{}".format(remainder), end="")
    else:
        remainder = number % 10
        print("{}".format(remainder), end="")
    return (remainder)
