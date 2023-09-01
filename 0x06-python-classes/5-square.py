#!/usr/bin/python3
"""define a class"""


class Square:
    """Square class with no attributes"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position=position

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size
    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    @position.setter
    def position(self, position):
        if not isinstance(position,tuple) or len(tuple) != 2 or not all(isinstance(num, int) for num in position) or not all(num>=0 for num in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position


    def my_print(self):
        if self.size == 0:
            print("")
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
