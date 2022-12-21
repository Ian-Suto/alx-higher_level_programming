#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """A class for finding the square of a number"""
    def __init__(self, size=0, position=(0, 0)):
        """A method square"""
        self.size = size
        self.position = position

    @property
    def position(self):
        """Getter method for the attribute position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for the attribute position"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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

    def my_print(self):
        """Print in stdout the square with the character #"""
        if self.__size == 0:
            print('')
        else:
            [print("") for i in range(0, self.__position[1])]
            for i in range(0, self.__size):
                [print(" ", end="") for j in range(0, self.__position[0])]
                [print("#", end="") for k in range(0, self.__size)]
                print("")
