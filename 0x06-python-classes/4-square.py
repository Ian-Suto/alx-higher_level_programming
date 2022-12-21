#!/usr/bin/python3
"""Module for calculating a number's square"""


class Square:
    """A class for finding the square of a number"""
    def __init__(self, size=0):
        """A method square"""
        self.size = size

    @property
    def size(self):
        """Getter method for the attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for the attribute size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the current square area"""
        return (self.__size**2)
