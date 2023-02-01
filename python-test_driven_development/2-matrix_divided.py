#!/usr/bin/python3
""" function that divides all elements of a matrix """


def matrix_divided(matrix, div):
    """ divide elements of a matrix by div and return a new matrix """
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if type(matrix) is not list or type(matrix[0]) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of \
                integers/floats")
    if (len(matrix) == 0) or (len(matrix[0]) == 0):
        raise TypeError("matrix must be a matrix (list of lists) of \
                integers/floats")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of \
                    integers/floats")
        for i in row:
            if type(i) is not int and type(i) is not float:
               raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats") 
    return [[round(i/div, 2) for i in row] for row in matrix]
