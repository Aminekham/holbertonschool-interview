#!/usr/bin/python3
"""
predicting the game output
"""


def isWinner(x, nums):
    """Determines the winner of the prime game"""

    if x == 0:
        return None
    max_n = max(nums)
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(max_n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False
    primes_count = [0] * (max_n + 1)
    count = 0
    for i in range(max_n + 1):
        if sieve[i]:
            count += 1
        primes_count[i] = count
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if primes_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
