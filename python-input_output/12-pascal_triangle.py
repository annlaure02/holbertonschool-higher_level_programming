#!/usr/bin/python3
""" Create a function pascal_triangle """


def pascal_triangle(n):
    """ returns a list of lists of integers representing 
the Pascal’s triangle of n """
    triangle = []
    lists = []
    if n <= 0:
        return []
    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            lists = [1]
            for j in range(1, i):
                lists.append(triangle[i - 1][j -1] + triangle[i - 1][j])
            lists.append(1)
            triangle.append(lists)
    return triangle
