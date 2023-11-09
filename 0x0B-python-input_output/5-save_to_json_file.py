#!/usr/bin/python3
"""Write an Object to a text file."""
import json


def save_to_json_file(my_obj, filename):
    """Write object to a file using json.

    Args:
    my_obj(obj):Object to write in to the file.
    filename(str):File to write to.
    """
    with open(filename, 'w+', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))
