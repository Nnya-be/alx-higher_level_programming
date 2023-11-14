#!/usr/bin/python3
"""Rectangle Model."""
from models.base import Base

class Rectangle(Base):
    """Class Rectangle Implementation."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class Constructor.

        Args:
        width(int): Positive integer.
        height(int): Positive integer.
        x(int): Positive integer.
        y(int): Positive integer.
        id(int): Positive integer.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def get_width(self):
        """Return private attribute width."""
        return self.__width

    @property
    def get_height(self):
        """Return private attribute height."""
        return self.__height

    @property
    def get_x(self):
        """Return private attribute x."""
        return self.__x

    @property
    def get_y(self):
        """Return private attribute y."""
        return self.__y

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter for width."""
        self.__validate_int("Width", width)
        self.__validate_positive("Width", width)
        self.__width = width

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter for height."""
        self.__validate_int("Height", height)
        self.__validate_positive("Height", height)
        self.__height = height

    @property
    def x(self):
        """Getter for x."""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter for x."""
        self.__validate_int("x", x)
        self.__x = x

    @property
    def y(self):
        """Getter for y."""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter for y."""
        self.__validate_int("y", y)
        self.__y = y

    def __validate_int(self, name, value):
        """Validate that the value is an integer."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

    def __validate_positive(self, name, value):
        """Validate that the value is positive."""
        if value < 0:
            raise ValueError(f"{name} must be a positive integer")
