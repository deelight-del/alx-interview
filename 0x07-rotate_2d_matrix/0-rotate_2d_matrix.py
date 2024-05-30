#!/usr/bin/python3
"""Module to solve rotating n X n matrix"""


def rotate_2d_matrix(matrix):
    """Function definiton."""

    if len(matrix) < 1:
        return
    # Transpose the each list in a matrix.
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
