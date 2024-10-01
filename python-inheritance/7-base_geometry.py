#!/usr/bin/python3
"""
This module defines a class BaseGeometry.
"""


class BaseGeometry:
    """
    A class to represent basic geometry operations.
    """

    def area(self):
        """
        Method that raises an exception as area is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the value is a positive integer.
        :param name: always a string.
        :param value: the value to validate.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
