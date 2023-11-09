#!/usr/bin/python3
"""Return a dictionary description with simple data structure."""
import json


def class_to_json(obj):
    """Json converter of objects."""
    return json.dumps(obj.__dict__)
