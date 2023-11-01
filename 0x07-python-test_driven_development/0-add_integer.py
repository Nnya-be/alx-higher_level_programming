#!/usr/bin/python3
"""Adding integers"""


def add_integer(a, b=98):
    """ Check if a and b are integers or floats.
    
    It also has test cases in the other files.
    """
    
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b
    """Returns the statement"""
    return a + b
