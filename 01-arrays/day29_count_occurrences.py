"""
Day 29: Count Occurrences in Sorted Array

Problem:
Find how many times a target appears in a sorted array.

Approach:
- Find first occurrence
- Find last occurrence
- Count = last - first + 1

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


def last_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


def count_occurrences(arr, target):
    first = first_occurrence(arr, target)
    last = last_occurrence(arr, target)

    if first == -1:
        return 0

    return last - first + 1


# Test
arr = [1,2,2,2,3,4,5]
target = 2

print("Count:", count_occurrences(arr, target))