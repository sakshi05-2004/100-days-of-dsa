"""
Day 81: BST Insertion
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


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


# Test
root = None

values = [5, 3, 7, 2, 4, 8]

for val in values:
    root = insert(root, val)

print("BST Inorder (Sorted):")
inorder(root)