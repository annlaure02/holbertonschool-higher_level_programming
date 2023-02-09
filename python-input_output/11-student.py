#!/usr/bin/python3
""" class Student """


class Student:
    """ class that define a student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        new_dict = {}
        if type(attrs) is list:
            for key, value in self.__dict__.items():
                for i in attrs:
                    if i == key:
                        new_dict[key] = value
            return new_dict
        return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
