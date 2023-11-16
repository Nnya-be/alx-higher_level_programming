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

    @classmethod
    def load_from_file(cls):
        """Load instances from a JSON file."""
        # Get the class name
        class_name = cls.__name__

        # Build the filename
        filename = f"{class_name}.json"

        try:
            with open(filename, 'r') as file:
                json_string = file.read()
        except FileNotFoundError:
            return []

        list_dicts = cls.from_json_string(json_string)
        return [cls.create(**d) for d in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save a list of objects to a CSV file."""
        if list_objs is None:
            list_objs = []

        # Get the class name
        class_name = cls.__name__

        # Build the filename
        filename = f"{class_name}.csv"

        with open(filename, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            for obj in list_objs:
                if class_name == "Rectangle":
                    csv_writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif class_name == "Square":
                    csv_writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Load instances from a CSV file."""
        # Get the class name
        class_name = cls.__name__

        # Build the filename
        filename = f"{class_name}.csv"

        try:
            with open(filename, 'r', newline='') as file:
                csv_reader = csv.reader(file)
                instances = []
                for row in csv_reader:
                    if class_name == "Rectangle":
                        instance = cls(int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]))
                    elif class_name == "Square":
                        instance = cls(int(row[0]), int(row[1]), int(row[2]), int(row[3]))
                    instances.append(instance)
        except FileNotFoundError:
            return []

        return instances
