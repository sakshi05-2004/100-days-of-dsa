"""
Day 85: Kth Smallest Element in BST
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, key):
    if not root:
        return Node(key)

    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root


def kth_smallest(root, k):

    stack = []
    current = root

    while True:

        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        k -= 1

        if k == 0:
            return current.data

        current = current.right


# Test
root = None
values = [5, 3, 7, 2, 4, 8]

for val in values:
    root = insert(root, val)

k = 3
print("Kth Smallest:", kth_smallest(root, k))