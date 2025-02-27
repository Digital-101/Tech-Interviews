class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def inorder_traversal(root):
    stack = []
    current = root
    result = []

    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            result.append(current.val)
            current = current.right
        else:
            break

    return result

# Example usage:
# Constructing the binary search tree
#         5
#        / \
#       3   7
#      / \ / \
#     2  4 6  8
#    /
#   1

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)
root.left.left.left = TreeNode(1)

print(inorder_traversal(root))  # Output: [1, 2, 3, 4, 5, 6, 7, 8]