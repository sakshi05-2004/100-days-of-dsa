"""
Day 26: Insertion Sort

Problem:
Sort an array using Insertion Sort.

Approach:
- Treat left portion as sorted
- Insert each element into correct position

Time Complexity: O(n^2)
Best Case: O(n)
Space Complexity: O(1)
"""

def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Shift elements greater than key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# Test
arr = [5, 3, 8, 4, 2]
print("Sorted Array:", insertion_sort(arr))