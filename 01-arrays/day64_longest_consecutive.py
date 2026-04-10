"""
Day 64: Longest Consecutive Sequence
"""

def longest_consecutive(nums):

    num_set = set(nums)
    max_length = 0

    for num in num_set:

        # Check if start of sequence
        if num - 1 not in num_set:

            current = num
            length = 1

            while current + 1 in num_set:
                current += 1
                length += 1

            max_length = max(max_length, length)

    return max_length


# Test
nums = [100, 4, 200, 1, 3, 2]

print("Longest Consecutive Length:", longest_consecutive(nums))