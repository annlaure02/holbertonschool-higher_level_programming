#!/usr/bin/python3
""" function that prints a text with 2 new lines after each 
    of these characters: ., ? and : """


def text_indentation(text):
    """ seperate a string from delimiter """
    if not isinstance(text, str):
       raise TypeError("text must be a string")

    delim = [".", "?", ":"]
    i = 0
    for line in text:
        if i == 0:
            if line == " ":
                continue
            else:
                i = 1
        if i == 1:
            if line in delim:
                print(line + "\n")
                i = 0
            else:
                print(line, end="")
