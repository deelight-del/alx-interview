#!/usr/bin/python3
"""Function to use backtracking"""

import sys


def generate_compromising_set(position, chess_length):
    """Function to generate the compromising positions on
    a chessboard, given the position"""
    compromising_set = set()
    compromising_set.update({
        (position[0], i)
        for i in range(chess_length)
    })
    compromising_set.update({
        (i, position[1])
        for i in range(chess_length)
    })
    compromising_set.update({
        (position[0] + 1 + i, position[1] + 1 + i)
        for i, _ in enumerate(range(position[1], chess_length - 1))
    })
    compromising_set.update({
        (position[0] - 1 - i, position[1] - 1 - i)
        for i, _ in enumerate(range(position[0], 0, -1))
    })
    left_diagonal = position[:]
    for i in range(chess_length):
        if left_diagonal[0] == chess_length - 1 or left_diagonal[1] == 0:
            break
        left_diagonal[0] = left_diagonal[0] + 1
        left_diagonal[1] = left_diagonal[1] - 1
        # print("left dia", left_diagonal)
        compromising_set.add(tuple(left_diagonal[:]))
        # print("compromising_list", compromising_list)
    left_diagonal = position[:]
    for i in range(chess_length):
        if left_diagonal[0] == 0 or left_diagonal[1] == chess_length - 1:
            break
        left_diagonal[0] = left_diagonal[0] - 1
        left_diagonal[1] = left_diagonal[1] + 1
        # print("left dia_r", left_diagonal)
        # print("position", position)
        compromising_set.add(tuple(left_diagonal[:]))
    return compromising_set


def find_non_compromising(remnant_chessboard, positions, chess_length):
    """Function to find non compromising positions
    on a chess board given positions that have already been
    occupied."""
    for postion in positions:
        compromising_set = generate_compromising_set(postion, chess_length)
        non_compromising_set = remnant_chessboard - compromising_set
        remnant_chessboard = non_compromising_set
    return non_compromising_set


def backtrack(positions, backtrack_no,
              chess_N, depth_visits_count, flag=False):
    """Function that accepts a position on the orginal
    chess board, pops the last element and replaces it
    with a value of the new remnant board"""
    # Remove the last element from positions.
    if all([
        depth_visits_count[i] >= chess_N**2 
        for i in range(chess_N)
    ]):
        return None, None, None
    new_positions = positions[:]
    [
        new_positions.pop() if len(new_positions)
        else ""
        for i in range(backtrack_no)
    ]
    original_chessboard = {
        (i, j) for i in range(chess_N)
        for j in range(chess_N)
    }
        # As a sorted list of members
    BASE_POSITIONS = [
                    [0, i]
                    for i in range(chess_N)
    ]
    if len(new_positions) == 0:
        new_positions = [BASE_POSITIONS[depth_visits_count[0]]]
    
    remnant_chessboard = find_non_compromising(original_chessboard,
                                               new_positions,
                                               chess_N)
    
    sorted_remnant_chessboard = (
                         sorted(list(remnant_chessboard),
                        key=lambda x: (x[0], x[1])))
    print("every backtrack depth visit count", depth_visits_count)
    try:
        revisit_count = depth_visits_count[len(new_positions)]
        return (
                new_positions + [list(sorted_remnant_chessboard[revisit_count])],
                remnant_chessboard, flag
        )
    except IndexError:
        depth_visits_count[len(new_positions) - 1] += 1
        return backtrack(new_positions, 0,
                         chess_N, depth_visits_count, flag=True)



def find_nqueen(remnant_chessboard, positions,
                chess_length, potential_positions, depth_visits_count,
                track_no=0, backtrack_no=0):
    print("pos for each recursion", positions)
    if len(positions) == chess_length:
        print(positions)
        return positions
    try:
        available_positions = list(find_non_compromising(remnant_chessboard,
                                                        positions +
                                                        [list(potential_positions[track_no])],
                                                        chess_length
                                                        ))
        print("available_positions for each recursion", available_positions)
#    if track_no < len(available_positions):
#        return find_nqueen(
#            remnant_chessboard,
#            positions + [list(available_positions[track_no])],
#            chess_length,
#            available_positions,
#            0,
#            backtrack_no
#        )
#
        if (len(available_positions) == 0):
            print("Here")
            return find_nqueen(remnant_chessboard, positions,
                            chess_length, potential_positions, depth_visits_count,
                            track_no + 1, backtrack_no)

        return find_nqueen(
            remnant_chessboard,
            positions + [list(available_positions[track_no])],
            chess_length,
            available_positions,
            depth_visits_count,
            0,
            backtrack_no
        )

    except IndexError:
        pass
    new_positions, new_remnant_chessboard, flag = backtrack(positions,
                                                            backtrack_no + 1,
                                                            chess_length,
                                                            depth_visits_count
                                                            )
    if new_positions is None:
        return None
    depth = len(new_positions) - 1
    depth_visits_count[depth] += 1
    return find_nqueen(
        new_remnant_chessboard,
        new_positions,
        chess_length,
        list(new_remnant_chessboard),
        depth_visits_count,
        0,
        (backtrack_no + 1 if not flag else 0),
    )


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
    # print("eventual list:", generate_compromising_set([2, 3], 5))
    original_chess = {
        (i, j) for i in range(chess_N)
        for j in range(chess_N)
    }
    initial_positions = [[0, 0]]
    potential_positions = list(find_non_compromising(original_chess,
                                                     initial_positions,
                                                     chess_N))
    depth_visits = {i: 0 for i in range(chess_N)}

    return find_nqueen(
        {tuple(ele) for ele in potential_positions},
        initial_positions,
        chess_N,
        potential_positions,
        depth_visits,
        0
    )



if __name__ == "__main__":
    print(main())
