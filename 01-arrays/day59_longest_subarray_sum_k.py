"""
Day 59: Longest Subarray with Sum K
"""

def longest_subarray_sum_k(arr, k):

    prefix_sum = 0
    max_length = 0

    prefix_map = {0: -1}

    for i in range(len(arr)):

        prefix_sum += arr[i]

        if (prefix_sum - k) in prefix_map:
            length = i - prefix_map[prefix_sum - k]
            max_length = max(max_length, length)

        # Store first occurrence only
        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i

    return max_length


# Test
arr = [1, 2, 3, 1, 1, 1, 1]
k = 3

print("Longest Length:", longest_subarray_sum_k(arr, k))