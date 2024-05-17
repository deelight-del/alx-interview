#!/usr/bin/python3
"""Function to use backtracking"""

import sys


def generate_compromising_list(position, chess_length):
    """Function to generate the compromising positions on
    a chessboard, given the position"""
    compromising_list = []
    compromising_list.extend([
        [position[0], i]
        for i in range(chess_length)
    ])
    compromising_list.extend([
        [i, position[1]]
        for i in range(chess_length)
    ])
    compromising_list.extend([
        [position[0] + 1 + i, position[1] + 1 + i]
        for i, _ in enumerate(range(position[1], chess_length - 1))
    ])
    compromising_list.extend([
        [position[0] - 1 - i, position[1] - 1 - i]
        for i, _ in enumerate(range(position[0], 0, -1))
    ])
    left_diagonal = position[:]
    for i in range(chess_length):
        if left_diagonal[0] == chess_length - 1 or left_diagonal[1] == 0:
            break
        left_diagonal[0] = left_diagonal[0] + 1
        left_diagonal[1] = left_diagonal[1] - 1
        # print("left dia", left_diagonal)
        compromising_list.append(left_diagonal[:])
        # print("compromising_list", compromising_list)
    left_diagonal = position[:]
    for i in range(chess_length):
        if left_diagonal[0] == 0 or left_diagonal[1] == chess_length - 1:
            break
        left_diagonal[0] = left_diagonal[0] - 1
        left_diagonal[1] = left_diagonal[1] + 1
        # print("left dia_r", left_diagonal)
        # print("position", position)
        compromising_list.append(left_diagonal[:])
    return compromising_list


def find_non_compromising(remnant_chessboard, positions, chess_length):
    """Function to find non compromising positions
    on a chess board given positions that have already been
    occupied."""
    for postion in positions:
        compromising_list = generate_compromising_list(postion, chess_length)
        ...

def main():
    """Main function to implement nquens"""
    if len(sys.argv) != 2:
        print("Usage nqueens N")
        exit(1)
    chess_N = sys.argv[1]
    if not chess_N.isdigit():
        print("N must be a number")
        exit(1)
    chess_N = int(chess_N)
    if chess_N < 4:
        print("N must be at least 4")
        exit(1)
    print("eventual list:", generate_compromising_list([2, 3], 5))


if __name__ == "__main__":
    main()
