#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """reprentation"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__width = size

    def area(self):
        return self.__size ** 2
