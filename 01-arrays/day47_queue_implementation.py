"""
Day 47: Implement Queue
"""

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0


# Test
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Front element:", q.peek())
print("Dequeued:", q.dequeue())
print("Queue after dequeue:", q.queue)