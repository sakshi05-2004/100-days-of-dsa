"""
Day 34: Reverse an Array using Recursion

Problem:
Reverse an array using recursion.

Approach:
- Swap first and last element
- Recursively reverse remaining subarray

Time Complexity: O(n)
Space Complexity: O(n)
"""

def reverse_array(arr, left, right):

    if left >= right:
        return

    arr[left], arr[right] = arr[right], arr[left]

    reverse_array(arr, left + 1, right - 1)


# Test
arr = [1, 2, 3, 4, 5]

reverse_array(arr, 0, len(arr) - 1)

print("Reversed Array:", arr)