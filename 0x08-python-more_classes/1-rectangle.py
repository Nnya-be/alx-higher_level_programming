#!/usr/bin/python3
"""A class definition of the rectangle class."""


class Rectangle:
    """Rectangle class definition and all its methods and attributes."""

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle class right after it is called.

        Args:
        width: It is of type int and not less than 0.
        width: It is of type int and not less than 0.

        Return:
        Does not return anything.

        Error:
        ValueError:When the values are less than 0.
        TypeError: When the values are not of type int.

        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Returns the valie of the width.

        Args:
        No argument.

        Return:
        __width: returns the value of __width.

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of the width.

        Args:
        value: It is used to set the width.

        Return:
        none.

        """
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
             if type(value) is not int:
                 raise TypeError("width must be an integer")
             self.__width = value

    @property
    def height(self):
        """Returns the value of the height.

        Args:
        none.

        Return:
        __height: Returns the height.

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of the height.

        Args:
        Value: Of type int and not less than 0.

        Return:
        none.

        Error:
        ValueError: when value is less than 0.
        TypeError: when the value is not an int.

        """
        if value < 0:
            raise ValueError("height must be >= 0")
        elif type(value) is not int:
            raise TypeError("height must be an integer")
        self.__height = value
