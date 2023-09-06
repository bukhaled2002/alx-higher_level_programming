#!/usr/bin/python3
"""Defines a Rectangle Class"""


class Rectangle:
    """Represent a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): the width
            height (int): the height
        """
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
                rect.append('#')
            if h != self.__height - 1:
                rect.append('\n')

        return ("".join(rect))
