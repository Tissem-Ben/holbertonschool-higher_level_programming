#!/usr/bin/python3
"""Shebang line indicating the interpreter for the script."""


class MyList(list):
    """A class that defines a list"""
    def print_sorted(self):
        """Prints a list."""
        sorted_list = sorted(self)
        print(sorted_list)
