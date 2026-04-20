"""
Day 74: Postorder Traversal (Binary Tree)
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


def postorder(node):

    if not node:
        return

    postorder(node.left)
    postorder(node.right)
    print(node.data, end=" ")


# Test
print("Postorder Traversal:")
postorder(root)