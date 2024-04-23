#!/usr/bin/python3
"""In this module, we work around trying
to solve the minimum operations challenge"""


import math
from typing import List


def isPrime(number: int) -> bool:
    """In this function, we check if a given
    number is True or not"""
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def getPrimeFactors(n: int) -> List[int]:
    """Function to return the available prime factors of
    a given integer as a list of integer"""
    if isPrime(n):
        return [1, n]
    return [
        i for i in range(2, int(math.sqrt(n)) + 1)
        if isPrime(i) and (n % i == 0)
    ]


def add_prime_factors(n: int) -> int:
    """Function to add prime factors"""
    if isPrime(n):
        return n
    highestPrimeFactor = getPrimeFactors(n)[-1]
    return highestPrimeFactor + add_prime_factors(n / highestPrimeFactor)


def minOperations(n):
    """The main function to evaluate minimum operations"""
    if n <= 0:
        return 0
    return int(add_prime_factors(n))
