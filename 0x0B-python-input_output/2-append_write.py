#!/usr/bin/python3
"""Append a string to the end of a file and returns the characters written."""


def append_write(filename="", text=""):
    """Append a string to the end of file.

    Args:
        filename(str):Name of file.
        text(str):String to append to file.

    Returns:
        length(int):The number of character written.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        file.seek(0, 2)
        length = file.write(text)
        return length
