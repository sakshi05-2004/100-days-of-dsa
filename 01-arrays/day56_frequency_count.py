"""
Day 56: Frequency Count using Hashing
"""

def frequency_count(arr):

    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    return freq


# Test
arr = [1, 2, 2, 3, 1, 4]

print("Frequency Count:", frequency_count(arr))