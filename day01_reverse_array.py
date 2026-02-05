"""
Day 1: Reverse an Array
Problem:
Given an array of integers, reverse the array.

Approach:
Use two pointers:
- One at the start
- One at the end
Swap elements and move pointers inward.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


# Testing the function
arr = [1, 2, 3, 4, 5]
print(reverse_array(arr))
