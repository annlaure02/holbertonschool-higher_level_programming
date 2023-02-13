#!/usr/bin/python3
""" creation of the class Base """


class Base:
    """ this class is a parent class """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
