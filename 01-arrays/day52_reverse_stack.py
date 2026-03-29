"""
Day 52: Reverse a Stack using Recursion
"""

def insert_at_bottom(stack, x):

    if not stack:
        stack.append(x)
        return

    top = stack.pop()
    insert_at_bottom(stack, x)

    stack.append(top)


def reverse_stack(stack):

    if not stack:
        return

    top = stack.pop()

    reverse_stack(stack)

    insert_at_bottom(stack, top)


# Test
stack = [1, 2, 3]

print("Original Stack:", stack)

reverse_stack(stack)

print("Reversed Stack:", stack)