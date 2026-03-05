"""
Day 28: Quick Sort

Problem:
Sort an array using Quick Sort.

Approach:
- Choose pivot
- Partition array around pivot
- Recursively sort left and right parts

Average Time Complexity: O(n log n)
Worst Case: O(n^2)
Space Complexity: O(log n)
"""

def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = []
    right = []

    for num in arr[:-1]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)

    return quick_sort(left) + [pivot] + quick_sort(right)


# Test
arr = [5,3,8,4,2]
print("Sorted Array:", quick_sort(arr))