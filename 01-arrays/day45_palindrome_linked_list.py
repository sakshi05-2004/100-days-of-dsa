"""
Day 45: Palindrome Linked List
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


def is_palindrome(head):

    if not head or not head.next:
        return True

    # Step 1: Find middle
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse second half
    second_half = reverse(slow)

    # Step 3: Compare
    first_half = head

    while second_half:
        if first_half.data != second_half.data:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True


# Test
head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(1)

print("Is Palindrome:", is_palindrome(head))