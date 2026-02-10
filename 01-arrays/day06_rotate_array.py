# Day 6: Rotate array by k positions

"""
Day 6: Rotate an Array by K Positions (Right Rotation)

Problem:
Given an array, rotate it to the right by k steps.

Approach:
- Reverse entire array
- Reverse first k elements
- Reverse remaining elements

Time Complexity: O(n)
Space Complexity: O(1)
"""

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def rotate_array(arr, k):
    n = len(arr)
    k = k % n

    reverse(arr, 0, n - 1)
    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)


# Test the function
arr = [1, 2, 3, 4, 5]
k = 2

rotate_array(arr, k)
print("Rotated array:", arr)

