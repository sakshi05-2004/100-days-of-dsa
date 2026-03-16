"""
Day 39: Delete Node from Linked List
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_node(head, key):

    # If head needs to be deleted
    if head and head.data == key:
        return head.next

    current = head

    # Traverse list
    while current.next and current.next.data != key:
        current = current.next

    # If node found
    if current.next:
        current.next = current.next.next

    return head


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

# Delete node
head = delete_node(head, 20)

print("After Deletion:")
print_list(head)