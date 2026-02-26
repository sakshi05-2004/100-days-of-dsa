"""
Day 21: Linear Search

Problem:
Given an array and a target element,
return the index of the target.
If not found, return -1.

Approach:
- Traverse array one by one
- Compare each element with target

Time Complexity: O(n)
Space Complexity: O(1)
"""

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Test
arr = [4, 2, 7, 1, 9]
target = 7

print("Index:", linear_search(arr, target))