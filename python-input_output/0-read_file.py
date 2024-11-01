#!/usr/bin/python3
"""Shebang line indicating the interpreter for the script."""


def read_file(filename=""):
    """Function that read a text file"""
    with open(filename, "r", encoding="UTF8",) as file:
        content = file.read()
        print(content, end="")
