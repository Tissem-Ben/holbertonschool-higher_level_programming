#!/usr/bin/python3
"""Shebang line indicating the interpreter for the script."""


def append_write(filename="", text=""):
    """Function that read a text file"""
    with open(filename, "a", encoding="UTF8",) as file:
        return (file.write(text))
