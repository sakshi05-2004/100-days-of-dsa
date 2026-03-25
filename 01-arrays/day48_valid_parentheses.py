"""
Day 48: Valid Parentheses using Stack
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
print(is_valid("()[]{}"))
print(is_valid("([)]"))