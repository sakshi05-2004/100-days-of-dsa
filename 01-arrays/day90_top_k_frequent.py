"""
Day 90: Top K Frequent Elements
"""

import heapq
from collections import Counter

def top_k_frequent(nums, k):

    freq = Counter(nums)

    heap = []

    for num, count in freq.items():

        heapq.heappush(heap, (count, num))

        if len(heap) > k:
            heapq.heappop(heap)

    return [num for count, num in heap]


# Test
nums = [1,1,1,2,2,3]
k = 2

print("Top K Frequent:", top_k_frequent(nums, k))