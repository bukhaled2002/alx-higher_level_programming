#!/usr/bin/python3
"""define a class"""


class Square:
    """Square class with no attributes"""

    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def my_print(self):
        if self.size == 0:
            print("")
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
                if (j == self.size - 1):
                    print("")
