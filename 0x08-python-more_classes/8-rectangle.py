#!/usr/bin/python3
"""Defines a Rectangle Class"""


class Rectangle:
    """Represent a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        if rect_2.area() > rect_1.area():
            return rect_2

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): the width
            height (int): the height
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Return area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Return perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """
        prints # with the height and width of the rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return ("")
        rect = []
        for h in range(self.__height):
            for w in range(self.__width):
                rect.append(str(self.print_symbol))
            if h != self.__height - 1:
                rect.append('\n')

        return ("".join(rect))

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
