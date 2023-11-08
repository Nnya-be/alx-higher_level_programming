#!/usr/bin/python3
"""Function to read a text file.

and print it to the stdout in the UTF-8 format.
"""


def read_file(filename=""):
    """Read The files using a loop.

    Args:
    filename: initialized to an empty string.
    Return:None
    """
    if filename is None:
        raise TypeError("No file name given:")
    with open(filename) as file:
        for lines in file:
            print(lines.strip())
