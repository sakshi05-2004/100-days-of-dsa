"""
Day 72: Inorder Traversal (Binary Tree)
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


def inorder(node):

    if not node:
        return

    inorder(node.left)
    print(node.data, end=" ")
    inorder(node.right)


# Test
print("Inorder Traversal:")
inorder(root)