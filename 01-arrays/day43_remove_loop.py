"""
Day 43: Remove Loop from Linked List
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_loop(head):

    slow = head
    fast = head

    # Step 1: Detect loop
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    else:
        return  # No loop

    # Step 2: Find start of loop
    slow = head

    while slow != fast:
        slow = slow.next
        fast = fast.next

    # Step 3: Remove loop
    loop_start = slow

    ptr = loop_start
    while ptr.next != loop_start:
        ptr = ptr.next

    ptr.next = None


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

# Create loop
head.next.next.next.next = head.next  # loop at 20

# Remove loop
remove_loop(head)

# Print list
print("After removing loop:")
print_list(head)