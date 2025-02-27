class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_lca(root, n1, n2):
    if root is None:
        return None

    if root.key == n1 or root.key == n2:
        return root

    left_lca = find_lca(root.left, n1, n2)
    right_lca = find_lca(root.right, n1, n2)

    if left_lca and right_lca:
        return root

    return left_lca if left_lca is not None else right_lca

# Example usage:
# Construct the binary tree
#         1
#        / \
#       2   3
#      / \ / \
#     4  5 6  7

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Test cases
print(find_lca(root, 4, 3).key)  # Output: 1
print(find_lca(root, 6, 7).key)  # Output: 3