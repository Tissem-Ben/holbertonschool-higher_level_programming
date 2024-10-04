#!/usr/bin/python3
"""Interpreter for the script."""

import json


def from_json_string(s):
    """Return a Python object from a JSON string."""
    return json.loads(s)
