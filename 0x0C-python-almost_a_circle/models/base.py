#!/usr/bin/python3
"""Base Model."""


class Base:
    """Class Base."""

    __nb_objects = 0
    def __init__(self, id=None):
        """Base Constructor."""
        if id is not None:
            self.__validate_id(id)
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def __validate_id(self, id):
        """Validate that id is a positive integer."""
        if not isinstance(id, int) or id <= 0:
            raise ValueError("id must be a positive integer")
