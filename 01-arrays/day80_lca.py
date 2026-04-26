"""
Day 80: Lowest Common Ancestor (Binary Tree)
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


def lca(root, p, q):

    if not root or root == p or root == q:
        return root

    left = lca(root.left, p, q)
    right = lca(root.right, p, q)

    if left and right:
        return root

    return left if left else right


# Test
p = root.left.left   # Node 4
q = root.left.right  # Node 5

ancestor = lca(root, p, q)

print("LCA:", ancestor.data)