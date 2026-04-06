"""
Day 60: Pair with Given Sum (Two Sum)
"""

def two_sum(arr, target):

    hashmap = {}

    for i, num in enumerate(arr):

        diff = target - num

        if diff in hashmap:
            return [hashmap[diff], i]

        hashmap[num] = i

    return []


# Test
arr = [2, 7, 11, 15]
target = 9

print("Indices:", two_sum(arr, target))