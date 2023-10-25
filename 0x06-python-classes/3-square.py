#!/usr/bin/python3
"""An implementation class for a square."""


class Square:
    """Class Square and it's definitions and attributes."""

    def __init__(self, size=0):
        """Initilize constructor for the square class.

        Args:
            size:(int) Must not be a negative value.

        Raises:
            TypeError: Whenever size is not a number.
            ValueError: Whenever size is a negative number.
        """
        try:
            if (not isinstance(size, int)):
                raise TypeError
            if (size < 0):
                raise ValueError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")

        self.__size = size

    def area(self):
        """Public Class method.

        Args:
            none.
        Return:
            return the current square area.
        """
        if (self.__size):
            return self.__size ** 2
