"""
Day 40: Reverse a Linked List
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_list(head):

    prev = None
    current = head

    while current:

        next_node = current.next
        current.next = prev

        prev = current
        current = next_node

    return prev


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

print("Original List:")
print_list(head)

# Reverse list
head = reverse_list(head)

print("Reversed List:")
print_list(head)