#!/usr/bin/python3
"""define a class"""


class Square:

    """Square class with no attributes"""
    def __init__(self, size=0):
        if not size.isdigit():
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
