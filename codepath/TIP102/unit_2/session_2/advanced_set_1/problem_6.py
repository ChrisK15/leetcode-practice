"""
Problem 6: Counting Divisible Collections in the Gallery

You have a list of integers collection_sizes representing the sizes of different art collections in your gallery and are trying to determine how to group them to best fit in your space. Given an integer k write a function count_divisible_collections() that returns the number of non-empty subarrays (contiguous parts of the array) where the sum of the sizes is divisible by k.

def count_divisible_collections(collection_sizes, k):
    pass

Example Usage:

nums1 = [4, 5, 0, -2, -3, 1]
k1 = 5
nums2 = [5]
k2 = 9

print(count_divisible_collections(nums1, k1))  
print(count_divisible_collections(nums2, k2))  

Example Output:

7
Example 1 Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

0
"""

def count_divisible_collections(collection_sizes, k):
    subarrays = []
    for i in range(len(collection_sizes)):
        for j in range(i, len(collection_sizes)):
            subarrays.append(collection_sizes[i:j+1])
    
    res = 0
    for subarray in subarrays:
        if sum(subarray) % k == 0:
            res += 1
    
    return res

nums1 = [4, 5, 0, -2, -3, 1]
k1 = 5
nums2 = [5]
k2 = 9

print(count_divisible_collections(nums1, k1))  
print(count_divisible_collections(nums2, k2)) 