#!/usr/bin/python3
"""Module to solve rotating n X n matrix"""


def rotate_2d_matrix(matrix):
    """Function definiton."""

    if len(matrix) < 1:
        return
    # Reverse the each list in a matrix.
    for i in range(len(matrix)):
        matrix[i].reverse()
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
