#!/usr/bin/python3
"""
This module defines a class Square.
"""


class Square:
    """
    This class represents a square with a private instance attribute: size.
    """

    def __init__(self, size):
        """
        Initialize the square with a private attribute size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size  # Private attribute
