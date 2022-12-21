#!/usr/bin/python3
"""Module for calculating a number's square"""


class Square:
    """A class for finding the square of a number"""
    def __init__(self, size=0):
        """A method square"""
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the current square area"""
        return (self.__size**2)
