"""
Day 71: Binary Tree Basics (Creation)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create tree manually
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


# Simple traversal (preorder)
def preorder(node):

    if not node:
        return

    print(node.data, end=" ")
    preorder(node.left)
    preorder(node.right)


# Test
print("Preorder Traversal:")
preorder(root)