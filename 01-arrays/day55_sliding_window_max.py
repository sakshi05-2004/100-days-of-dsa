"""
Day 55: Sliding Window Maximum
"""

from collections import deque

def max_sliding_window(nums, k):

    dq = deque()
    result = []

    for i in range(len(nums)):

        # Remove elements out of window
        if dq and dq[0] == i - k:
            dq.popleft()

        # Remove smaller elements
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        # Add result when window is full
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


# Test
arr = [1,3,-1,-3,5,3,6,7]
k = 3

print("Sliding Window Maximum:", max_sliding_window(arr, k))