#!/usr/bin/python3

""" Module to solve the prime game challenge.
"""


def sieve_of_n(n):
    """sieve_of_n is a function that
    determines who wins between Maria and Ben.
    of a given `n`.
    """
    if (n <= 0):
        return -1
    if (n == 1):
        return 'Ben'
    playing_round = 0
    prime_number_idx = 1
    sieve = [i + 1 for i in range(n)]
    while sieve[prime_number_idx] < (n / 2) + 1:
        prime_number = sieve[prime_number_idx]
        for number in sieve[prime_number_idx + 1:]:
            if number % prime_number == 0:
                sieve.remove(number)
        prime_number_idx += 1
        playing_round += 1
    prime_number_idx -= 1
    playing_round += len(sieve[prime_number_idx:])
    # if playing_round == 0:
    #    return -1
    if playing_round % 2:
        return 'Ben'
    return 'Maria'


def isWinner(x, nums):
    """Uses sieve_of_n to determine eventual winner in x round
    of the game."""

    rounds_win = [sieve_of_n(num) for num in nums]
    maria_count = rounds_win.count('Maria')
    ben_count = rounds_win.count('Ben')
    if maria_count == ben_count:
        return None
    if maria_count > ben_count:
        return 'Maria'
    return 'Ben'
