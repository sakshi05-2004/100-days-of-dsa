"""
Day 51: Implement Queue using Stack
"""

class QueueUsingStack:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        if not self.stack2:

            # Move elements to stack2
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:
            return "Queue is empty"

        return self.stack2.pop()

    def peek(self):
        if not self.stack2:

            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:
            return "Queue is empty"

        return self.stack2[-1]

    def is_empty(self):
        return not self.stack1 and not self.stack2


# Test
q = QueueUsingStack()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Front:", q.peek())
print("Dequeued:", q.dequeue())
print("After dequeue:", q.stack1, q.stack2)