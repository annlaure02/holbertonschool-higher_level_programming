#!/usr/bin/python3
""" Unittest for class Rectangle
"""
import unittest
from io import StringIO
from contextlib import redirect_stdout
from models.rectangle import Rectangle
from models.base import Base


class Test_Rectangle(unittest.TestCase):
    """ unittest to check class Rectangle"""
    def test_init(self):
        """ tests instance attributes """
        r = Rectangle(8, 6, 4, 2, 18)
        self.assertEqual(r.id, 18)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 2)

    def test_type_error_init(self):
        """ tests error messages value is not int """
        self.assertRaisesRegex(TypeError, "width must be an integer",
                               Rectangle, "8", 6, 4, 2, 10)
        self.assertRaisesRegex(TypeError, "height must be an integer",
                               Rectangle, 8, "6", 4, 2, 10)
        self.assertRaisesRegex(TypeError, "x must be an integer",
                               Rectangle, 8, 6, "4", 2, 10)
        self.assertRaisesRegex(TypeError, "y must be an integer",
                               Rectangle, 8, 6, 4, "2", 10)

    def test_value_error_init(self):
        """ tests error messages value is not les than 0 """
        self.assertRaisesRegex(ValueError, "width must be > 0",
                               Rectangle, -8, 6, 4, 2, 10)
        self.assertRaisesRegex(ValueError, "width must be > 0",
                               Rectangle, 0, 6, 4, 2, 10)
        self.assertRaisesRegex(ValueError, "height must be > 0",
                               Rectangle, 2, 0, 4, 2, 10)
        self.assertRaisesRegex(ValueError, "height must be > 0",
                               Rectangle, 8, -6, 4, 2, 10)
        self.assertRaisesRegex(ValueError, "x must be >= 0",
                               Rectangle, 8, 6, -4, 2, 10)
        self.assertRaisesRegex(ValueError, "y must be >= 0",
                               Rectangle, 8, 6, 4, -2, 10)

    def test_area(self):
        """ tests area value of the rectangle """
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r2.area(), 56)

    def test_str(self):
        """ test methos __str__ """
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display(self):
        """ tests to print the rectangle with # """
        r = Rectangle(4, 2)
        output = '####\n####\n'
        with StringIO() as buffer, redirect_stdout(buffer):
            r.display()
            res = buffer.getvalue()
        self.assertEqual(res, output)

        r1 = Rectangle(5, 3, 1, 1)
        output = '\n #####\n #####\n #####\n'
        with StringIO() as buffer, redirect_stdout(buffer):
            r1.display()
            res = buffer.getvalue()
        self.assertEqual(res, output)

    def test_update_args(self):
        """ tests update method to assigns argument to attribute """
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)
        r.update(89, 20)
        self.assertEqual(r.width, 20)

    def test_update_kwargs(self):
        """ test update assigns a key/value argument to attributes """
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(r.height, 1)

    def test_to_dictionary(self):
        """ tests methode dictionary """
        r = Rectangle(2, 4, 6, 8, 22)
        self.assertEqual(r.to_dictionary(), {'id': 22, 'width': 2, 'height': 4,
                                             'x': 6, 'y': 8})

if __name__ == '__main__':
    unittest.main()
