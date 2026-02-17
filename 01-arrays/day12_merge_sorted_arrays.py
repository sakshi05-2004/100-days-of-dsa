"""
Day 12: Merge Two Sorted Arrays

Problem:
Given two sorted arrays, merge them into one sorted array.

Approach:
- Use two pointers
- Compare elements and append smaller one
- Add remaining elements after loop

Time Complexity: O(n + m)
Space Complexity: O(n + m)
"""

def merge_sorted_arrays(arr1, arr2):
    i = 0
    j = 0
    merged = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # Add remaining elements
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged


# Test
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]

print("Merged Array:", merge_sorted_arrays(arr1, arr2))

# return

