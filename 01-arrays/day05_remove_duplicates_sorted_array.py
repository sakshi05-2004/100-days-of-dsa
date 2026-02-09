"""
Day 5: Remove Duplicates from a Sorted Array

Problem:
Given a sorted array, remove duplicates in-place
and return the count of unique elements.

Approach:
- Use two pointers
- One pointer tracks unique elements
- Another pointer scans the array

Time Complexity: O(n)
Space Complexity: O(1)
"""

def remove_duplicates(arr):
    if len(arr) == 0:
        return 0

    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]

    return i + 1


# Test the function
arr = [1, 1, 2, 2, 3, 3, 3, 4]
k = remove_duplicates(arr)

print("Unique count:", k)
print("Array after removing duplicates:", arr[:k])

