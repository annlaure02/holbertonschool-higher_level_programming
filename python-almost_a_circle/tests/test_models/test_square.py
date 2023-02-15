#!/usr/bin/python3
""" Unittest for class Square
"""
import unittest
from io import StringIO
from contextlib import redirect_stdout
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class Test_Rectangle(unittest.TestCase):
    """ unittest to check class Square """
    def test_init(self):
        """ tests instance attributes """
        s = Square(8, 6, 4, 2)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 8)
        self.assertEqual(s.x, 6)
        self.assertEqual(s.y, 4)

    def test_type_error_init(self):
        """ tests error messages value is not int """
        self.assertRaisesRegex(TypeError, "width must be an integer",
                               Square, "6", 4, 2, 10)
        self.assertRaisesRegex(TypeError, "x must be an integer",
                               Square, 6, "4", 2, 10)
        self.assertRaisesRegex(TypeError, "y must be an integer",
                               Square, 6, 4, "2", 10)

    def test_value_error_init(self):
        """ tests error messages value is not les than 0 """
        self.assertRaisesRegex(ValueError, "width must be > 0",
                               Square, -8, 6, 4, 10)
        self.assertRaisesRegex(ValueError, "width must be > 0",
                               Square, 0, 6, 4, 10)
        self.assertRaisesRegex(ValueError, "x must be >= 0",
                               Square, 8, -6, 2, 10)
        self.assertRaisesRegex(ValueError, "y must be >= 0",
                               Square, 8, 6, -2, 10)

    def test_area(self):
        """ tests area value of the rectangle """
        s1 = Square(3)
        self.assertEqual(s1.area(), 9)

        s2 = Square(8, 0, 0, 12)
        self.assertEqual(s2.area(), 64)

    def test_str(self):
        """ test methos __str__ """
        s = Square(4, 2, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 4")

    def test_display(self):
        """ tests to print the rectangle with # """
        s = Square(4)
        output = '####\n####\n####\n####\n'
        with StringIO() as buffer, redirect_stdout(buffer):
            s.display()
            res = buffer.getvalue()
        self.assertEqual(res, output)

        s1 = Square(5, 1, 1)
        output = '\n #####\n #####\n #####\n #####\n #####\n'
        with StringIO() as buffer, redirect_stdout(buffer):
            s1.display()
            res = buffer.getvalue()
        self.assertEqual(res, output)

    def test_update_args(self):
        """ tests update method to assigns argument to attribute """
        s = Square(10, 10, 10, 10)
        s.update(89)
        self.assertEqual(s.id, 89)
        s.update(89, 20)
        self.assertEqual(s.size, 20)

    def test_update_kwargs(self):
        """ test update assigns a key/value argument to attributes """
        s = Square(10, 10, 10, 10)
        s.update(size=1)
        self.assertEqual(s.size, 1)

    def test_to_dictionary(self):
        """ tests methode dictionary """
        s = Square(4, 6, 8, 22)
        self.assertEqual(s.to_dictionary(), {'id': 22, 'size': 4,
                                             'x': 6, 'y': 8})

    def test_create(self):
        """ test method create """
        s = Square.create(**{'id': 5, 'size': 6,'x': 2, 'y': 1})
        s1 = Square(6, 2, 1, 5)
        self.assertIsNot(s, s1)

if __name__ == '__main__':
    unittest.main()
