"""
Day 77: Count Leaf Nodes
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


def count_leaves(node):

    if not node:
        return 0

    # Check leaf
    if not node.left and not node.right:
        return 1

    return count_leaves(node.left) + count_leaves(node.right)


# Test
print("Leaf Nodes Count:", count_leaves(root))