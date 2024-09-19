#!/usr/bin/python3
"""
This module defines a Square class with size validation,
area calculation, and getter/setter methods for the size attribute.
"""


class Square:
    """
    This class represents a square with a private instance attribute: size.
    """

    def __init__(self, size=0):
        """
        Initialize the square with a private attribute size and validate it.

        Args:
            size (int): The size of the square, must be an integer and >= 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size  # Use the setter for validation

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square, with validation for type and value.

        Args:
            value (int): The size of the square, must be an integer and >= 0.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Compute and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
