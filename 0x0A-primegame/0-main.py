#!/usr/bin/python3

isWinner1 = __import__('1-prime-game').isWinner
isWinner0 = __import__('0-prime_game').isWinner


print("Expected Winner: {}".format(isWinner1(5, [2, 5, 1, 4, 3])))
print("Seen Winner: {}".format(isWinner0(5, [2, 5, 1, 4, 3])))
print("Expected Winner: {}".format(isWinner1(1, [9200])))
print("Seen Winner: {}".format(isWinner0(1, [9200])))
print("Expected Winner: {}".format(isWinner1(5, [9200, 1000, 876, 667])))
print("Seen Winner: {}".format(isWinner0(1, [9200, 1000, 876, 667])))
print("Expected Winner: {}".format(isWinner1(1, [2])))
print("Seen Winner: {}".format(isWinner0(1, [2])))
