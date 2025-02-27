class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root):
    def checkHeight(node):
        if not node:
            return 0
        leftHeight = checkHeight(node.left)
        if leftHeight == -1:
            return -1
        rightHeight = checkHeight(node.right)
        if rightHeight == -1:
            return -1
        if abs(leftHeight - rightHeight) > 1:
            return -1
        return max(leftHeight, rightHeight) + 1

    return checkHeight(root) != -1

# Example usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(4)
print(isBalanced(root))  # Output: False