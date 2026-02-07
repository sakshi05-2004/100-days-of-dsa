"""
Day 3: Find the Second Largest Element in an Array

Problem:
Given an array of integers, find the second largest element.

Approach:
- Maintain two variables: largest and second_largest
- Traverse the array once and update them accordingly

Time Complexity: O(n)
Space Complexity: O(1)
"""

def second_largest(arr):
    if len(arr) < 2:
        return None

    largest = float('-inf')
    second_largest = float('-inf')

    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num != largest and num > second_largest:
            second_largest = num

    return second_largest


# Test the function
arr = [10, 5, 20, 8]
print("Second Largest:", second_largest(arr))
