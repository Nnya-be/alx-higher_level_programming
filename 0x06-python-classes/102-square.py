#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square.

    Attributes:
        __size (int): size of a side of the square.
    """

    def __init__(self, size=0):
        """Initialize the square.

        Args:
            size (int): size of a side of the square.
        Returns:
            None.
        """
        self.size = size

    def area(self):
        """Calculate the square's area.

        Returns:
            The area of the square.
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """Getter of __size.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Getter of __size.

        Args:
            value: (int) The value to set with.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")

            self.__size = value

    def __eq__(self, other):
        """Equal to method.

        Args:
            other: (Class Square) the other class.
        Return:
            Return true if equal else otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Not Equal to method.

        Args:
            other: (Class Square) the other class.
        Return:
            Return false if equal else otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """Greater than to method.

        Args:
            other: (Class Square) the other class.
        Return:
            Return true if Greater else otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater or Equal to method.

        Args:
            other: (Class Square) the other class.
        Return:
            Return true if equal or greater else otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """Less Than to method.

        Args:
            other: (Class Square) the other class.
        Return:
            Return true if less than else otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """Less or Equal to method.

        Args:
            other: (Class Square) the other class.
        Return:
            Return true if less or equal else otherwise.
        """
        return self.area() <= other.area()
