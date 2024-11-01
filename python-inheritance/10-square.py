#!/usr/bin/python3
"""Shebang line indicating the interpreter for the script."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a new instance"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return (self.__size * self.__size)
