#!/usr/bin/python3
"""A program to validate the size of a square."""


class Square:
    """A Class Implementation of a square."""

    def __init__(self, size=0):
        """Initialize function for the class square.

        Args: size of type int and returns nothing.
        """
        try:
            if (size < 0):
                raise ValueError
            if (not isinstance(size, int)):
                raise TypeError

            self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
