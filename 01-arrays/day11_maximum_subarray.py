"""
Day 11: Maximum Subarray (Kadane's Algorithm)

Problem:
Find the contiguous subarray with the maximum sum.

Approach:
- Use Kadane's Algorithm
- Maintain current_sum and max_sum
- Reset current_sum if it becomes negative

Time Complexity: O(n)
Space Complexity: O(1)
"""

def max_subarray(nums):
    max_sum = float('-inf')
    current_sum = 0

    for num in nums:
        current_sum += num

        if current_sum > max_sum:
            max_sum = current_sum

        if current_sum < 0:
            current_sum = 0

    return max_sum


# Test
nums = [-2,1,-3,4,-1,2,1,-5,4]
print("Maximum Subarray Sum:", max_subarray(nums))


