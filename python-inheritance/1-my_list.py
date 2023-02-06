#!/usr/bin/python3
""" Write a class MyList that inherits from list """


class MyList(list):
    """ print sorted list """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
