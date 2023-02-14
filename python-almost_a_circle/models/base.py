#!/usr/bin/python3
""" creation of the class Base """
import json


class Base:
    """ this class is a parent class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialisation of id """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or list_dictionaries == "":
            return "[]"
        else:
            return json.dumps(list_dictionaries)
            
