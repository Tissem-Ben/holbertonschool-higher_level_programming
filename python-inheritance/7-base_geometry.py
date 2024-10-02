#!/usr/bin/python3
"""Defines a class BaseGeometry"""

class BaseGeometry:
    """A class with basic geometric functions"""

    def area(self):
        """Raises an Exception with a message indicating that the method is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that 'value' is an integer greater than 0

        Args:
            name (str): The name of the parameter (just a string to display in the error message)
            value (int): The value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
