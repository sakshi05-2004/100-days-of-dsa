"""
Day 50: Implement Stack using Queue
"""

from collections import deque

class StackUsingQueue:

    def __init__(self):
        self.queue = deque()

    def push(self, x):
        self.queue.append(x)

        # Rotate queue
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.queue.popleft()

    def top(self):
        if self.is_empty():
            return "Stack is empty"
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0


# Test
s = StackUsingQueue()

s.push(10)
s.push(20)
s.push(30)

print("Top:", s.top())
print("Pop:", s.pop())
print("After pop:", list(s.queue))