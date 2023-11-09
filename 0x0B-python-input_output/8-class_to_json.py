#!/usr/bin/python3
"""Return a dictionary description with simple data structure."""


def class_to_json(obj):
    """Json converter of objects."""
    return obj.__dict__
