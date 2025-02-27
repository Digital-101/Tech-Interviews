class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root, left=float('-inf'), right=float('inf')):
    if not root:
        return True
    if not (left < root.val < right):
        return False
    return (is_valid_bst(root.left, left, root.val) and
            is_valid_bst(root.right, root.val, right))

# Example usage:
# Valid BST
root_valid = TreeNode(2)
root_valid.left = TreeNode(1)
root_valid.right = TreeNode(3)

# Invalid BST
root_invalid = TreeNode(5)
root_invalid.left = TreeNode(1)
root_invalid.right = TreeNode(4)
root_invalid.right.left = TreeNode(3)
root_invalid.right.right = TreeNode(6)

print(is_valid_bst(root_valid))  # Output: True
print(is_valid_bst(root_invalid))  # Output: False