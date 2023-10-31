#!/usr/bin/python3
"""A class definition of the rectangle class."""


class Rectangle:
    number_of_instances = 0

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
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Returns the valie of the width.

        Args:
        No argument.

        Return:
        __width: returns the value of __width.

        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """Set the value of the width.

        Args:
        value: It is used to set the width.

        Return:
        none.

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Returns the value of the height.

        Args:
        none.

        Return:
        __height: Returns the height.

        """
        return (self.__height)

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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculate the value of the area of the rectangle.

        Args:
        None

        Return:
        Area of the rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculate the value of the perimeter of the rectangle.

        Args:
        None

        Return:
        Perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """Print the rectangle.

        Args:
        None

        Return:
        None
        """
        str = ''
        if self.__width == 0 or self.__height == 0:
            return str
        for i in range(self.__height):
            for i in range(self.__width):
                str += "#"
            str += '\n'
        str = str[0:-1]
        return str

    def __repr__(self):
        """Print the rectangle.

        Args:
        None

        Return:
        None
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Destructor of the rectangle."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
