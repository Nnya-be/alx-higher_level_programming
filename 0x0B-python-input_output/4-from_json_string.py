#!/usr/bin/python3
"""Return an object represented by JSON string."""
import json


def from_json_string(my_str):
    """Return an object.

    Args:
    my_str(str):JSON string.

    Returns:
    my_str(obj):Object form of my_str.
    """
    my_obj = json.loads(my_str)
    return my_obj
