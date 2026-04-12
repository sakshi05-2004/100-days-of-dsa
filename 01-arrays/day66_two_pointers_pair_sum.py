"""
Day 66: Pair Sum using Two Pointers
"""

def pair_sum(arr, target):

    left = 0
    right = len(arr) - 1

    while left < right:

        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return [arr[left], arr[right]]

        elif current_sum < target:
            left += 1

        else:
            right -= 1

    return []


# Test
arr = [2, 3, 4, 7, 11]
target = 9

print("Pair:", pair_sum(arr, target))