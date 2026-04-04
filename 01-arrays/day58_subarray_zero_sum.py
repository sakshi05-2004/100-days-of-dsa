"""
Day 58: Subarray with Zero Sum
"""

def has_zero_sum_subarray(arr):

    prefix_sum = 0
    seen = set()

    for num in arr:

        prefix_sum += num

        if prefix_sum == 0 or prefix_sum in seen:
            return True

        seen.add(prefix_sum)

    return False


# Test
arr1 = [4, 2, -3, 1, 6]
arr2 = [1, 2, 3]

print("Has Zero Sum Subarray:", has_zero_sum_subarray(arr1))
print("Has Zero Sum Subarray:", has_zero_sum_subarray(arr2))