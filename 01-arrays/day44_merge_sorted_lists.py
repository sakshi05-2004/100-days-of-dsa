"""
Day 44: Merge Two Sorted Linked Lists
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def merge_lists(l1, l2):

    dummy = Node(0)
    current = dummy

    while l1 and l2:

        if l1.data < l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next

        current = current.next

    # Attach remaining nodes
    if l1:
        current.next = l1
    else:
        current.next = l2

    return dummy.next


def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


# Create first list
l1 = Node(1)
l1.next = Node(3)
l1.next.next = Node(5)

# Create second list
l2 = Node(2)
l2.next = Node(4)
l2.next.next = Node(6)

# Merge lists
merged_head = merge_lists(l1, l2)

print("Merged List:")
print_list(merged_head)