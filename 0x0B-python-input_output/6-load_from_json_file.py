#!/usr/bin/python3
"""Create an Object from a JSON file."""
import json


def load_from_json_file(filename):
    """A function that creates an object from a json file.

    Args:
    filename(str):The file to read from.
    """
    with open(filename) as file:
        return json.load(file)
