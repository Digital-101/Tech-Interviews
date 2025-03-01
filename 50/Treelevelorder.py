from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def level_order_traversal(root):
    if not root:
        return
    
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        print(node.value, end=' ')
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Example usage:
# Constructing the tree:
#         1
#        / \
#       2   3
#      / \ / \
#     4  5 6  7

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.right.left = TreeNode(6)
tree.right.right = TreeNode(7)

level_order_traversal(tree)