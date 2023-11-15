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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """Representation of the class."""
        return (
            "[Rectangle] ({}) ".format(self.id) +
            "{}/{} - {}/{}".format(self.x, self.y, self.width, self.height)
        )

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter for width."""
        self.__validate_int("width", width)
        self.__validate_positive("width", width)
        self.__width = width

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter for height."""
        self.__validate_int("height", height)
        self.__validate_positive("height", height)
        self.__height = height

    @property
    def x(self):
        """Getter for x."""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter for x."""
        self.__validate_int("x", x)
        self.__validate_non_negative("x", x)
        self.__x = x

    @property
    def y(self):
        """Getter for y."""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter for y."""
        self.__validate_int("y", y)
        self.__validate_non_negative("y", y)
        self.__y = y

    def __validate_int(self, name, value):
        """Validate that the value is an integer."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

    def __validate_positive(self, name, value):
        """Validate that the value is positive."""
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    def __validate_non_negative(self, name, value):
        """Validate that the value is non-negative."""
        if value < 0:
            raise ValueError(f"{name} must be >= 0")

    def area(self):
        """Calculate Area of a rectangle instance."""
        return (self.__height * self.__width)

    def display(self):
        """Print the rectangle."""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def update(self, *args, **kwargs):
        """Assign args to attributes in order."""
        if args:
            if len(args) >= 1:
                super().__init__(args[0])
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    super().__init__(value)
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        """Return the dictionary representation of the Rectangle."""
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }
