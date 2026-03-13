"""
Day 36: Create a Singly Linked List

Problem:
Create a linked list and print its elements.

Approach:
- Create a Node class
- Link nodes together
- Traverse and print values

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# Link nodes
node1.next = node2
node2.next = node3
node3.next = node4

# Head of list
head = node1


# Traverse and print list
current = head

while current:
    print(current.data, end=" -> ")
    current = current.next

print("None")