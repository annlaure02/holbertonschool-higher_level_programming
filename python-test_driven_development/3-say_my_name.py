#!/usr/bin/python3
""" prints My name is <first name> <last name> """


def say_my_name(first_name, last_name=""):
    """ print a string with 2 variable who has to be string """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
