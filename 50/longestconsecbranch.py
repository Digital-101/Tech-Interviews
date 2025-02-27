class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def longest_consecutive(root):
    def helper(node, parent_val, length):
        if not node:
            return length
        if node.val == parent_val + 1:
            length += 1
        else:
            length = 1
        left_length = helper(node.left, node.val, length)
        right_length = helper(node.right, node.val, length)
        return max(length, left_length, right_length)

    if not root:
        return 0
    return helper(root, root.val - 1, 0)

# Example usage:
# Constructing the tree:
#     1
#      \
#       2
#        \
#         3
root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)

print(longest_consecutive(root))  # Output: 3