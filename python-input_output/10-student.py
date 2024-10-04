#!/usr/bin/python3
"""
Defines a Student class with attributes for name and age.
"""


class Student:
    """
    A class that represents a student.

    Attributes:
        first_name (str): First name.
        last_name (str): Last name.
        age (int): Age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student.

        Args:
            first_name (str): First name.
            last_name (str): Last name.
            age (int): Age.
        """
        self.first_name = first_name  # First name
        self.last_name = last_name    # Last name
        self.age = age                # Age

    def to_json(self, attrs=None):
        """
        Gets dict representation of a Student.

        Args:
            attrs (list): Attributes to retrieve (optional).

        Returns:
            dict: Representation of the student.
        """
        if attrs is None:
            return self.__dict__  # All attributes
        return {attr: self.__dict__[attr]
                for attr in attrs if attr in self.__dict__}  # Filtered
