#!/usr/bin/python3
""" function that reads a text file and prints it to stdout  """


def read_file(filename=""):
    """ read the text with open """
    with open(filename, encoding="utf-8") as f:
        read = f.read()
        print(read)
