#!/usr/bin/python3
"""Shebang line indicating the interpreter for the script."""


class Student:
    """Class Student"""
    def __init__(self, first_name, last_name, age):
        """init method for public instances attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        data_dict = self.__dict__
        new_dict = {}
        if attrs is not None:
            for key, value in data_dict.items():
                if key in attrs:
                    new_dict[key] = value
            return new_dict
        return data_dict

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
