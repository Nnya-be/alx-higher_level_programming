#!/usr/bin/python3
"""Base Model."""
import json


class Base:
    """Class Base."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Class Base Constructor."""
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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of objects to a JSON file."""
        if list_objs is None:
            list_objs = []

        # Get the class name
        class_name = cls.__name__

        # Build the filename
        filename = f"{class_name}.json"

        # Convert instances to dictionaries
        list_dicts = [obj.to_dictionary() for obj in list_objs]

        # Convert dictionaries to JSON string
        json_string = cls.to_json_string(list_dicts)

        # Write JSON string to file
        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON string to a list of dictionaries."""
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with attributes set from a dictionary."""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            return None

        dummy_instance.update(**dictionary)
        return dummy_instance
