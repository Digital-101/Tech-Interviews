import random

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.size = 1

    def insert(self, value):
        if value <= self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)
        self.size += 1

    def get_random_node(self):
        left_size = self.left.size if self.left else 0
        index = random.randint(0, self.size - 1)
        if index < left_size:
            return self.left.get_random_node()
        elif index == left_size:
            return self
        else:
            return self.right.get_random_node()

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self.root.insert(value)

    def get_random_node(self):
        if self.root is None:
            return None
        return self.root.get_random_node()

# Example usage:
if __name__ == "__main__":
    tree = BinaryTree()
    values = [5, 3, 8, 1, 4, 7, 9]
    for value in values:
        tree.insert(value)

    print(tree.get_random_node().value)
    print(tree.get_random_node().value)
    print(tree.get_random_node().value)