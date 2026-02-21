"""
Day 16: First Non-Repeating Character

Problem:
Given a string, return the first non-repeating character.
If none exists, return None.

Approach:
- Count frequency of each character
- Traverse string again to find first character with frequency 1

Time Complexity: O(n)
Space Complexity: O(1)
"""

def first_non_repeating(s):
    count = {}

    # First pass: count characters
    for char in s:
        count[char] = count.get(char, 0) + 1

    # Second pass: find first non-repeating
    for char in s:
        if count[char] == 1:
            return char

    return None


# Test
print(first_non_repeating("leetcode"))
print(first_non_repeating("aabb"))