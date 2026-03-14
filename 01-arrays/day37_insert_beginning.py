"""
Day 37: Insert Node at Beginning of Linked List
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_at_beginning(head, data):

    new_node = Node(data)

    new_node.next = head

    return new_node


def print_list(head):

    current = head

    while current:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


# Create initial list
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

print("Original List:")
print_list(head)

# Insert new node
head = insert_at_beginning(head, 5)

print("After Insertion:")
print_list(head)