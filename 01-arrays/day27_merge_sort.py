"""
Day 27: Merge Sort

Problem:
Sort an array using Merge Sort.

Approach:
- Divide array into halves
- Recursively sort
- Merge sorted arrays

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):

    result = []
    i = j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Test
arr = [5,3,8,4,2]
print("Sorted Array:", merge_sort(arr))