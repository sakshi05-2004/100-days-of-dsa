"""
Day 24: Bubble Sort

Problem:
Sort an array using Bubble Sort.

Approach:
- Compare adjacent elements
- Swap if needed
- Repeat for all elements

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


# Test
arr = [5, 3, 8, 4, 2]
print("Sorted Array:", bubble_sort(arr))