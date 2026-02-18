"""
Day 13: Reverse a String

Problem:
Given a string, return its reversed version.

Approach:
- Convert string to list
- Use two pointers to swap characters
- Join back into string

Time Complexity: O(n)
Space Complexity: O(n)
"""

def reverse_string(s):
    chars = list(s)
    left = 0
    right = len(chars) - 1

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return "".join(chars)


# Test
print(reverse_string("hello"))
