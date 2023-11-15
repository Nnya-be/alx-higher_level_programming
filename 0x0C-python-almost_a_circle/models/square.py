#!/usr/bin/python3
"""Square Module."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Class Constructor.

        Args:
        size(int): Positive integer.
        x(int): Positive integer.
        y(int): Positive integer.
        id(int): Positive integer.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size."""
        self.width = value
        self.height = value

    def __str__(self):
        """Representation String of the Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
