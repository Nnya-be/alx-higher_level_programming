#!/usr/bin/python3
"""Function to read a text file.

and print it to the stdout in the UTF-8 format.
"""


def read_file(filename=""):
    """Read the content of a text file to the stdout.

    Args:
        filename(str): Name of the file to read.
    
    Returns:
        None

    Raises:
        IOError: If there exits an issue reading the file.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                print(line.strip())
    except IOError:
        raise IOError(f"Error reading file '{filename}':")
        
