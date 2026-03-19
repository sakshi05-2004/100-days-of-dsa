"""
Day 42: Detect Loop in Linked List
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def has_cycle(head):

    slow = head
    fast = head

    while fast and fast.next:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# Create linked list
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

# Create a loop (point last node to second node)
head.next.next.next.next = head.next

# Check loop
print("Loop Detected:", has_cycle(head))