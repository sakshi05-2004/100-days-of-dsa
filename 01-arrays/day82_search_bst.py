"""
Day 82: Search in BST
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


def search(root, key):

    if not root:
        return False

    if root.data == key:
        return True

    elif key < root.data:
        return search(root.left, key)

    else:
        return search(root.right, key)


# Test
root = None
values = [5, 3, 7, 2, 4, 8]

for val in values:
    root = insert(root, val)

print("Search 4:", search(root, 4))
print("Search 10:", search(root, 10))