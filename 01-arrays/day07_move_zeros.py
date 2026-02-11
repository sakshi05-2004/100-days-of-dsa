"""
Day 7: Move All Zeros to the End

Problem:
Given an array, move all zeros to the end while maintaining
the order of non-zero elements.

Approach:
- Use two pointers
- Swap non-zero elements forward

Time Complexity: O(n)
Space Complexity: O(1)
"""

def move_zeros(arr):
    i = 0

    for j in range(len(arr)):
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1


# Test the function
arr = [0, 1, 0, 3, 12]
move_zeros(arr)

print("After moving zeros:", arr)
