#!/usr/bin/python3
"""In this module we try to solve the lock
boxes challenge"""


def canUnlockAll(boxes):
    """Function to evaluate is given lockboxes
    can be fully opened"""
    if not (isinstance(boxes, list) and len(boxes) > 0):
        return False
    boxUnlocked = [False] * len(boxes)
    boxUnlocked[0] = True
    for i in range(len(boxes)):
        for j in range(len(boxes)):
            if boxUnlocked[j]:
                keys = boxes[j]
                for k in keys:
                    if k < len(boxUnlocked):
                        boxUnlocked[k] = True
    if sum(boxUnlocked) == len(boxes):
        return True
    return False
