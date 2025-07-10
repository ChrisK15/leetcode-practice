"""
Problem 4: Count Winning Pairings

In a popular reality TV show, contestants pair up for various challenges. The pairing is considered winning if the sum of their "star power" is a power of two.

You are given an array of integers star_power where star_power[i] represents the star power of the i-th contestant. Return the number of different winning pairings you can make from this list, modulo 10^9 + 7.

Note that contestants with different indices are considered different even if they have the same star power.

def count_winning_pairings(star_power):
    pass

Example Usage:

star_power1 = [1, 3, 5, 7, 9]
print(count_winning_pairings(star_power1))

star_power2 = [1, 1, 1, 3, 3, 3, 7]
print(count_winning_pairings(star_power2))

Example Output:

4
15
"""

from collections import Counter

def count_winning_pairings(star_power):
    pass


star_power1 = [1, 3, 5, 7, 9]
print(count_winning_pairings(star_power1))

star_power2 = [1, 1, 1, 3, 3, 3, 7]
print(count_winning_pairings(star_power2))