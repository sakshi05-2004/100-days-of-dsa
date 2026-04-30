"""
Day 84: Validate Binary Search Tree
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_valid_bst(root, low=float('-inf'), high=float('inf')):

    if not root:
        return True

    if not (low < root.data < high):
        return False

    return (is_valid_bst(root.left, low, root.data) and
            is_valid_bst(root.right, root.data, high))


# Test
root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.right.left = Node(4)  # Invalid case

print("Is Valid BST:", is_valid_bst(root))