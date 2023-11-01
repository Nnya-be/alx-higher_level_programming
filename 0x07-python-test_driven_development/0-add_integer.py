#!/usr/bin/python3
"""Adding integers."""


def add_integer(a, b=98):
    """Check if a and b are integers or floats.

    It also has test cases in the other files.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    elif a is True or a is False:
        raise TypeError("a must be an integer")
    elif b is True or b is False:
        raise TypeError("b must be an integer")
    else:
        a = int(a) if isinstance(a, float) else a
        b = int(b) if isinstance(b, float) else b
    """Returns the statement"""
    return a + b
