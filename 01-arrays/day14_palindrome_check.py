"""
Day 14: Check if a String is Palindrome

Problem:
Given a string, determine if it is a palindrome.

Approach:
- Use two pointers
- Compare characters from both ends
- Return False on mismatch

Time Complexity: O(n)
Space Complexity: O(1)
"""

def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


# Test
print(is_palindrome("madam"))
print(is_palindrome("hello"))



