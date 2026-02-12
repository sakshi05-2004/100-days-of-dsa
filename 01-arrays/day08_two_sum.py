"""
Day 8: Two Sum

Problem:
Given an array of integers and a target value,
return the indices of two numbers that add up to the target.

Approach:
- Use a hash map (dictionary)
- Store numbers and their indices
- For each number, check if (target - number) exists

Time Complexity: O(n)
Space Complexity: O(n)
"""

def two_sum(nums, target):
    hashmap = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in hashmap:
            return [hashmap[complement], i]

        hashmap[num] = i


# Test
nums = [2, 7, 11, 15]
target = 9

print("Indices:", two_sum(nums, target))



