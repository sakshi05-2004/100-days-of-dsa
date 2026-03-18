"""
Day 41: Find Middle of Linked List
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def find_middle(head):

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


# Create list
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

print("Linked List:")
print_list(head)

# Find middle
middle = find_middle(head)

print("Middle Element:", middle.data)