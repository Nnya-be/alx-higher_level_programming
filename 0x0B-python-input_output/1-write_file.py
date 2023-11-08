#!/usr/bin/python3
"""Write a string to a text file and returns the number of characters."""


def write_file(filename="", text=""):
    """Print and return the number of Texts written.

    Args:
        filename(str): File name to write to.
        text(str): The string to write.

    Returns:
        length(int):The number of characters written.
    """
    with open(filename, 'w') as file:
        length = file.write(text)
        return length
