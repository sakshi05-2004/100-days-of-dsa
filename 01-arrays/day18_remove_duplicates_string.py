"""
Day 18: Remove Duplicates from a String

Problem:
Given a string, remove duplicate characters
while keeping the first occurrence.

Approach:
- Use a set to track seen characters
- Build result string only with unseen characters

Time Complexity: O(n)
Space Complexity: O(n)
"""

def remove_duplicates(s):
    seen = set()
    result = ""

    for char in s:
        if char not in seen:
            seen.add(char)
            result += char

    return result


# Test
print(remove_duplicates("programming"))