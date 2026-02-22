"""
Day 17: Longest Common Prefix

Problem:
Given a list of strings, return the longest common prefix.

Approach:
- Use the first word as reference
- Compare characters vertically across all strings
- Stop at first mismatch

Time Complexity: O(n * m)
n = number of strings
m = length of shortest string
Space Complexity: O(1)
"""

def longest_common_prefix(strs):
    if not strs:
        return ""

    prefix = strs[0]

    for i in range(len(prefix)):
        for word in strs[1:]:
            if i >= len(word) or word[i] != prefix[i]:
                return prefix[:i]

    return prefix


# Test
print(longest_common_prefix(["flower", "flow", "flight"]))

print(longest_common_prefix(["dog", "racecar", "car"]))


