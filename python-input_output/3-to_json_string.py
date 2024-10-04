#!/usr/bin/python3
"""Shebang line indicating the interpreter for the script."""


import json


def to_json_string(my_obj):
    """Function that return a text file"""
    return json.dumps(my_obj)
