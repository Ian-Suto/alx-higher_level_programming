#!/usr/bin/python3
"""An empty class representing a rectangle"""


class Rectangle:
    """An example of a class, representing a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.
        Args:
            width (int): The rectangle width
            height (int): The rectangle height
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def height(self):
        """Getter method for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height attribute"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Getter method for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width attribute"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Return rectangle area"""
        return (self.__width*self.__height)

    def perimeter(self):
        """Return rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2*(self.__width+self.__height))

    def __str__(self):
        """Return a rectangle representation built with the character #"""
        if self.__height == 0 or self.__width == 0:
            return ("")
        r = []
        for i in range(self.__height):
            list(r.append(str(self.print_symbol)) for i in range(self.__width))
            if i != (self.__height - 1):
                r.append("\n")
        return (''.join(r))

    def __repr__(self):
        """Return string representation of a rectangle"""
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        """Delete instance"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle based on area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)
