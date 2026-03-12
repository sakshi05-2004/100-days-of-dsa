"""
Day 35: Palindrome Check using Recursion

Problem:
Check if a string is palindrome using recursion.

Approach:
- Compare first and last characters
- Recursively check inner substring

Time Complexity: O(n)
Space Complexity: O(n)
"""

def is_palindrome(s, left, right):

    if left >= right:
        return True

    if s[left] != s[right]:
        return False

    return is_palindrome(s, left + 1, right - 1)


# Test
word = "madam"

print("Is Palindrome:", is_palindrome(word, 0, len(word) - 1))