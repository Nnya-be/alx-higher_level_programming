import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_initialization(self):
        rectangle = Rectangle(10, 20, 5, 8, 1)

        self.assertEqual(rectangle.id, 1)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 20)
        self.assertEqual(rectangle.x, 5)
        self.assertEqual(rectangle.y, 8)

    def test_set_width(self):
        rectangle = Rectangle(10, 20, 5, 8, 1)

        # Test positive integer
        rectangle.width = 15
        self.assertEqual(rectangle.width, 15)

        # Test invalid (non-integer)
        with self.assertRaises(TypeError):
            rectangle.width = "invalid"

        # Test invalid (negative)
        with self.assertRaises(ValueError):
            rectangle.width = -5

    def test_set_height(self):
        rectangle = Rectangle(10, 20, 5, 8, 1)

        # Test positive integer
        rectangle.height = 25
        self.assertEqual(rectangle.height, 25)

        # Test invalid (non-integer)
        with self.assertRaises(TypeError):
            rectangle.height = "invalid"

        # Test invalid (negative)
        with self.assertRaises(ValueError):
            rectangle.height = -5

    def test_set_x(self):
        rectangle = Rectangle(10, 20, 5, 8, 1)

        # Test integer
        rectangle.x = 10
        self.assertEqual(rectangle.x, 10)

        # Test invalid (non-integer)
        with self.assertRaises(TypeError):
            rectangle.x = "invalid"

    def test_set_y(self):
        rectangle = Rectangle(10, 20, 5, 8, 1)

        # Test integer
        rectangle.y = 15
        self.assertEqual(rectangle.y, 15)

        # Test invalid (non-integer)
        with self.assertRaises(TypeError):
            rectangle.y = "invalid"

if __name__ == '__main__':
    unittest.main()
