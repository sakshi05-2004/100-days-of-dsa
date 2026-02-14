
"""
Day 10: Majority Element

Problem:
Find the element that appears more than n/2 times.

Approach:
Use Boyer-Moore Voting Algorithm.
Maintain a candidate and count.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def majority_element(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


# Test
nums = [2, 2, 1, 1, 1, 2, 2]
print("Majority Element:", majority_element(nums))




