#!/usr/bin/python3
"""Making Change Module"""


def makeChange(coins, total):
    """Function to implement make change problem"""
    coins_copy = coins[:]
    coins_copy.sort(reverse=True)
    change = 0
    for i in range(len(coins_copy)):
        while total >= coins_copy[i]:
            total -= coins_copy[i]
            change += 1
            if total == 0:
                return change
    return -1
