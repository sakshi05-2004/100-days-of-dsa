"""
Day 87: K Largest Elements
"""

import heapq

def k_largest(nums, k):

    min_heap = []

    for num in nums:

        heapq.heappush(min_heap, num)

        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap


# Test
arr = [3, 2, 1, 5, 6, 4]
k = 2

print("K Largest Elements:", k_largest(arr, k))