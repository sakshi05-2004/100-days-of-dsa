"""
Day 15: Valid Anagram

Problem:
Given two strings, check if one is an anagram of the other.

Approach:
- If lengths differ, return False
- Use dictionary to count characters
- Decrease count while iterating second string

Time Complexity: O(n)
Space Complexity: O(1)  # since character set is limited
"""

def is_anagram(s, t):
    if len(s) != len(t):
        return False

    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1

    for char in t:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False

    return True


# Test
print(is_anagram("anagram", "nagaram"))
print(is_anagram("rat", "car"))