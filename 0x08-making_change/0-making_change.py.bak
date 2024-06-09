#!/usr/bin/python3
"""Making Change Module"""


def optimal_solution(coin_list, slice_of_solution):
    """Helper function to find the minimum value of
    the ith_value"""
    sub_sum = len(slice_of_solution)
    counts_per_position = []
    for deno in coin_list:
        pos_on_slice = sub_sum - deno
        if (pos_on_slice >= 0 and
           slice_of_solution[pos_on_slice] >= 0):
            counts_per_position.append(slice_of_solution[pos_on_slice] + 1)
    if len(counts_per_position) == 0:
        return -1
    return min(counts_per_position)


def makeChange(coins, total):
    """Function to implement make change problem"""
    if total <= 0:
        return 0
    solution_list = [total + total for _ in range(total + 1)]
    solution_list[0] = 0
    for i in range(1, len(solution_list)):
        ith_value = optimal_solution(coins, solution_list[0:i])
        # if ith_value <= 0:
        #    return -1
        solution_list[i] = ith_value
    return solution_list[-1]
