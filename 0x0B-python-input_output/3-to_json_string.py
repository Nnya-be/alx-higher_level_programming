#!/usr/bin/python3
"""Return JSON representation of an object."""
import json


def to_json_string(my_obj):
    """Return the JSON format of an object.

    Args:
    my_obj(obj):The object to change to json.

    Returns:
    my_json(json): The json form of my_obj.
    """
    my_json = json.dumps(my_obj)
    return my_json
