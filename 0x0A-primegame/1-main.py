#!/usr/bin/python3
"""Testing for 10,000"""

import random

isWinner = __import__('0-prime_game').isWinner

test_array = [ random.randint(0, 10000) for _ in range(5000)]

print('The winner is: ', isWinner(5000, test_array))
