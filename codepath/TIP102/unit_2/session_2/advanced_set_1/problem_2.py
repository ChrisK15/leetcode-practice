"""
Problem 2: Verifying Authenticity

Your art gallery has just been shipped a new collection of numbered art pieces, and you need to verify their authenticity. The collection is considered "authentic" if it is a permutation of an array base[n].

The base[n] array is defined as [1, 2, ..., n - 1, n, n], meaning it is an array of length n + 1 containing the integers from 1 to n - 1 exactly once, and the integer n twice. For example, base[1] is [1, 1] and base[3] is [1, 2, 3, 3].

Write a function is_authentic_collection that accepts an array of integers art_pieces and returns True if the given array is an authentic array, and otherwise returns False.

Note: A permutation of integers represents an arrangement of these numbers. For example [3, 2, 1] and [2, 1, 3] are both permutations of the series of numbers 1, 2, and 3.

def is_authentic_collection(art_pieces):
    pass

Example Usage:

collection1 = [2, 1, 3]
collection2 = [1, 3, 3, 2]
collection3 = [1, 1]

print(is_authentic_collection(collection1))
print(is_authentic_collection(collection2))
print(is_authentic_collection(collection3))
"""

from collections import Counter

def is_authentic_collection(art_pieces):
    n = len(art_pieces) - 1
    d = Counter(art_pieces)
    
    if d.get(n, 0) != 2:
        return False
    
    if len(d) != n:  # Should only have n distinct numbers total
        return False
    
    for i in range(1, n):  # This goes from 1 to n-1
        if d.get(i, 0) != 1: # Should appear exactly once
            return False
    
    return True