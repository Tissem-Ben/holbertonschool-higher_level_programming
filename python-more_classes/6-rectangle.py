#!/usr/bin/python3
"""Shebang line indicating the interpreter for the script."""


class Rectangle:
    """Class representing a rectangle with width and height attributes."""

    number_of_instances = 0  # Class attribute to count instances

    def __init__(self, width=0, height=0):
        """a new Rectangle instance with optional width and height."""
        self.width = width
        self.height = height
