#!/usr/bin/python3
"""Function to read a text file and print it to the stdout
in the UTF-8 format.
"""

def read_file(filename=""):
    with open(filename) as file:
        for lines in file:
            print(lines.strip())
