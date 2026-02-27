"""
Day 22: Binary Search

Problem:
Given a sorted array and a target,
return the index of target.
If not found, return -1.

Approach:
- Use two pointers (left and right)
- Check middle element
- Narrow search space by half each time

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Test
arr = [1, 3, 5, 7, 9, 11]
target = 7

print("Index:", binary_search(arr, target))