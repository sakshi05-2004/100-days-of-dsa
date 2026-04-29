"""
Day 83: Delete Node in BST
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


def find_min(node):
    while node.left:
        node = node.left
    return node


def delete_node(root, key):

    if not root:
        return root

    if key < root.data:
        root.left = delete_node(root.left, key)

    elif key > root.data:
        root.right = delete_node(root.right, key)

    else:
        # Case 1 & 2
        if not root.left:
            return root.right

        elif not root.right:
            return root.left

        # Case 3: two children
        temp = find_min(root.right)
        root.data = temp.data
        root.right = delete_node(root.right, temp.data)

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

print("Before Deletion:")
inorder(root)

root = delete_node(root, 3)

print("\nAfter Deletion:")
inorder(root)