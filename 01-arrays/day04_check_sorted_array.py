# Day 4: Check if an array is sorted
"""
Day 4: Check if an Array is Sorted

Problem:
Given an array of integers, check whether it is sorted in non-decreasing order.

Approach:
- Traverse the array
- Compare each element with the next one
- If any element is greater than the next, return False
- If loop completes, return True

Time Complexity: O(n)
Space Complexity: O(1)
"""

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


# Test the function
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 3, 2, 4]

print("Array 1 sorted?", is_sorted(arr1))
print("Array 2 sorted?", is_sorted(arr2))

