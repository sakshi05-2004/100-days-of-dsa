"""
Day 57: First Repeating Element
"""

def first_repeating(arr):

    seen = set()

    for num in arr:

        if num in seen:
            return num

        seen.add(num)

    return None


# Test
arr1 = [1, 2, 3, 2, 1]
arr2 = [1, 2, 3, 4]

print("First Repeating:", first_repeating(arr1))
print("First Repeating:", first_repeating(arr2))