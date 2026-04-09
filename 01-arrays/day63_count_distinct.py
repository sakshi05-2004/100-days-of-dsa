"""
Day 63: Count Distinct Elements
"""

def count_distinct(arr):

    return len(set(arr))


# Test
arr = [1, 2, 2, 3, 4, 4, 5]

print("Distinct Count:", count_distinct(arr))