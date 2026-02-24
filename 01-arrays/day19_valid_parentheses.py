"""
Day 19: Valid Parentheses

Problem:
Check if the input string of brackets is valid.

Approach:
- Use stack
- Push opening brackets
- Match closing brackets with top of stack

Time Complexity: O(n)
Space Complexity: O(n)
"""

def is_valid(s):
    stack = []
    mapping = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()

    return len(stack) == 0


# Test
print(is_valid("()"))
print(is_valid("()[]{}"))
print(is_valid("(]"))
print(is_valid("([)]"))