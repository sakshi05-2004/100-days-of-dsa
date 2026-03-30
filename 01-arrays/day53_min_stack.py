"""
Day 53: Min Stack
"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)

        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if not self.stack:
            return "Stack is empty"

        val = self.stack.pop()

        if val == self.min_stack[-1]:
            self.min_stack.pop()

        return val

    def top(self):
        if not self.stack:
            return "Stack is empty"
        return self.stack[-1]

    def get_min(self):
        if not self.min_stack:
            return "Stack is empty"
        return self.min_stack[-1]


# Test
s = MinStack()

s.push(5)
s.push(2)
s.push(8)
s.push(1)

print("Min:", s.get_min())  # 1
s.pop()
print("Min after pop:", s.get_min())  # 2