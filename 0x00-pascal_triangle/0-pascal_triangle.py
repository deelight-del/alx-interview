#!/usr/bin/python3
"""In this module, we construct the helper Function
and actual function for deriving a pascal triangle"""


def helpPascal(array):
    """Helper Function for pascal triangle"""
    newPascal = [1]
    for i, v in enumerate(array[:-1]):
        newPascal.append(
            v + array[i + 1]
        )
    newPascal.append(1)
    return newPascal


def pascal_triangle(n):
    """The main function that implements pascal triangle"""
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]
    finalArray = [[1], [1, 1]]
    for i in range(2, n):
        finalArray += [helpPascal(finalArray[-1])]
    return finalArray
