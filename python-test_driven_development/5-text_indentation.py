#!/usr/bin/python3
""" function that prints a text with 2 new lines after each 
    of these characters: ., ? and : """


def text_indentation(text):
    """ seperate a string from delimiter """
    if not isinstance(text, str):
       raise TypeError("text must be a string")

    delim = [".", "?", ":"]
    a = 0
    while a < len(text):
        if text[a] in delim:
            print(text[a])
            print()
            a += 1
        else:
            print(text[a], end='')
        a += 1
