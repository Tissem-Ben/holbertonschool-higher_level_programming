#!/usr/bin/python3
"""Shebang line indicating the interpreter for the script."""


def write_file(filename="", text=""):
    """Function that read a text file"""
    with open(filename, "w", encoding="UTF8",) as file:
        return (file.write(text))
