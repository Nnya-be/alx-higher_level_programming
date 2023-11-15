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

    def __str__(self):
        """Representation String of the Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
