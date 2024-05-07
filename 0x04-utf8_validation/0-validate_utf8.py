#!/usr/bin/python3
"""Utf-8 validation module"""


def validUTF8(data):
    """Implementation of valid UTF-8 function"""
    remnant = 0
    for num in data:
        if remnant > 0:
            if num >> 6 != 0b10:
                return False
            remnant -= 1
        else:
            if num >> 5 == 0b110:
                remnant = 2
            elif num >> 4 == 0b1110:
                remnant = 3
            elif num >> 3 == 0b11110:
                remnant = 4
            elif num >> 7 == 0b0:
                continue
            else:
                return False
    return remnant == 0
