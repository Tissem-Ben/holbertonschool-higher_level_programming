#!/usr/bin/python3
"""
This module defines a class Square with size validation.
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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  # Private attribute
