"""
Day 73: Preorder Traversal (Binary Tree)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Build tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


def preorder(node):

    if not node:
        return

    print(node.data, end=" ")
    preorder(node.left)
    preorder(node.right)


# Test
print("Preorder Traversal:")
preorder(root)