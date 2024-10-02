#!/usr/bin/python3
"""Shebang line indicating the interpreter for the script."""


class BaseGeometry:
    """Defines a class name's BaseGeometry"""
    def area(self):
        """Method to raise an exception if area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that the value is an integer and greater than 0"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
