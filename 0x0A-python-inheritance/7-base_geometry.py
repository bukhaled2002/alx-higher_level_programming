#!/usr/bin/python3
"""Defines an empty class BaseGeometry."""


class BaseGeometry:
    """this is comment"""

    def area(self):
        raise Exception("area() is not implemented")
  
    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
