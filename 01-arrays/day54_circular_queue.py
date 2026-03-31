"""
Day 54: Circular Queue
"""

class CircularQueue:

    def __init__(self, k):
        self.size = k
        self.queue = [0] * k
        self.front = -1
        self.rear = -1

    def enqueue(self, value):

        # Check full
        if (self.rear + 1) % self.size == self.front:
            return "Queue is full"

        # First element
        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value

    def dequeue(self):

        if self.front == -1:
            return "Queue is empty"

        val = self.queue[self.front]

        # Only one element
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        return val

    def display(self):

        if self.front == -1:
            print("Queue is empty")
            return

        i = self.front

        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size

        print()


# Test
q = CircularQueue(5)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

print("Queue:")
q.display()

print("Dequeued:", q.dequeue())

print("After dequeue:")
q.display()