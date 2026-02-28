"""
Day 23: First and Last Occurrence using Binary Search

Problem:
Find first and last position of target in sorted array.

Approach:
- Use modified binary search twice
- Once for first occurrence
- Once for last occurrence

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def find_first(arr, target):
    left, right = 0, len(arr) - 1
    first = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            first = mid
            right = mid - 1  # search left side
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return first


def find_last(arr, target):
    left, right = 0, len(arr) - 1
    last = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            last = mid
            left = mid + 1  # search right side
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return last


def find_first_last(arr, target):
    return [find_first(arr, target), find_last(arr, target)]


# Test
arr = [1,2,2,2,3,4,5]
target = 2

print("First and Last:", find_first_last(arr, target))