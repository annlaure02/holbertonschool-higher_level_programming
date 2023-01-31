#!/usr/bin/python3
""" function that adds 2 integers """


def add_integer(a, b=98):
    """ add 2 integers or floats and return an interer """
    if type(a) is not int and type(a) is not float:
        b = int(b)
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
