import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_increment_id(self):
        base1 = Base()
        base2 = Base()

        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_custom_id(self):
        base_with_custom_id = Base(42)

        self.assertEqual(base_with_custom_id.id, 42)

    def test_negative_custom_id(self):
        with self.assertRaises(ValueError) as context:
            Base(-5)

        self.assertEqual(str(context.exception), "id must be a positive integer")

    def test_string_custom_id(self):
        with self.assertRaises(ValueError) as context:
            Base("a_string")

        self.assertEqual(str(context.exception), "id must be a positive integer")


if __name__ == '__main__':
    unittest.main()
