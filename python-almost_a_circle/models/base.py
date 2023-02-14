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

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                dict_list = [obj.to_dictionary() for obj in list_objs]
                json_string = cls.to_json_string(dict_list)
                f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """ return the list of the JSON string representation json_string """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)
