"""
Day 20: Longest Substring Without Repeating Characters

Problem:
Find the length of the longest substring without repeating characters.

Approach:
- Use sliding window technique
- Maintain set of characters
- Expand right pointer and shrink left when duplicate found

Time Complexity: O(n)
Space Complexity: O(n)
"""

def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


# Test
print(length_of_longest_substring("abcabcbb"))
print(length_of_longest_substring("bbbbb"))