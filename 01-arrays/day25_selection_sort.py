"""
Day 25: Selection Sort

Problem:
Sort an array using Selection Sort.

Approach:
- Find minimum element
- Swap with current position
- Repeat for all elements

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# Test
arr = [5, 3, 8, 4, 2]
print("Sorted Array:", selection_sort(arr))