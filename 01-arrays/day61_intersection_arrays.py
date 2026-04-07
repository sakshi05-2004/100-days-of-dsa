"""
Day 61: Intersection of Two Arrays
"""

def intersection(arr1, arr2):

    set1 = set(arr1)
    set2 = set(arr2)

    return list(set1 & set2)


# Test
arr1 = [1, 2, 2, 1]
arr2 = [2, 2]

print("Intersection:", intersection(arr1, arr2))