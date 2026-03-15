"""
Day 38: Insert Node at End of Linked List
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_at_end(head, data):

    new_node = Node(data)

    # If list is empty
    if head is None:
        return new_node

    current = head

    # Traverse until last node
    while current.next:
        current = current.next

    current.next = new_node

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

# Insert at end
head = insert_at_end(head, 50)

print("After Insertion:")
print_list(head)