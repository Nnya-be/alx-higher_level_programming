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
        self.__size = size

    def area(self):
        """Public Class method.

        Args:
            none.
        Return:
            return the current square area.
        """
        return self.__size ** 2
    
    @property
    def size(self):
        """getter of __size
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")

            self.__size = value

    def my_print(self):
        """A Method for printing the squre

        Args:
            none
        Return:
            none
        """
        if (self.__size == 0):
            print()
        else:
            for i in range(self.__size):
                for x in range(self.__size):
                    print("#", end='')
                print("")
