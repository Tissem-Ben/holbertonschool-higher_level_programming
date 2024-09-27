#!/usr/bin/python3
"""Shebang line indicating the interpreter for the script"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance otherwise returns False"""
    return isinstance(obj, a_class) and type(obj) is not a_class
