#!/usr/bin/python3
"""A program to validate the size of a square."""


class Square:
    """A Class Implementation of a square."""

    def __init__(self, size=0):
        """Initialize constructor function for the class square.

        Args:
             size(int): The size of the square. I must be non-negative.

        Raises:
              TypeError: If the size is not an integer.
              ValueError: If the size is negative.
        """
        try:
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            if (size < 0):
                raise ValueError("size must be >= 0")
        finally:
            self.__size = size
