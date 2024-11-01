#!/usr/bin/python3
"""Shebang line indicating the interpreter for the script."""


class BaseGeometry:
    """Defines a class named BaseGeometry."""

    def area(self):
        """Raises an Exception if the method is unimplemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Args:
            name (str): Parameter name for error messages.
            value (int): Value to validate.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
