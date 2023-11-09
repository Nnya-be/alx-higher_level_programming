#!/usr/bin/python3
"""Student Module."""


class Student:
    """Student Class."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student object with first_name, last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student instance."""
        if attrs is None:
            return self.__dict__

        student_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                student_dict[attr] = getattr(self, attr)
        return student_dict
