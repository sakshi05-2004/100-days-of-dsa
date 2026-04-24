"""
Day 78: Diameter of Binary Tree
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


def diameter(root):

    max_diameter = 0

    def height(node):
        nonlocal max_diameter

        if not node:
            return 0

        left = height(node.left)
        right = height(node.right)

        # Update diameter
        max_diameter = max(max_diameter, left + right)

        return 1 + max(left, right)

    height(root)
    return max_diameter


# Test
print("Diameter:", diameter(root))