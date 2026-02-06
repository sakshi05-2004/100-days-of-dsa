"""
Day 2: Find Maximum and Minimum in an Array

Problem:
Given an array of integers, find the maximum and minimum elements.

Approach:
- Assume first element as max and min
- Traverse the array and update max and min accordingly

Time Complexity: O(n)
Space Complexity: O(1)
"""

def find_max_min(arr):
    max_val = arr[0]
    min_val = arr[0]

    for num in arr:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

    return max_val, min_val


# Test the function
arr = [3, 1, 5, 2, 4]
max_value, min_value = find_max_min(arr)
print("Max:", max_value)
print("Min:", min_value)
