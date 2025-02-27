import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def tree_to_doubly_list(root):
    if not root:
        return None

    first, last = [None], [None]  # Using lists to hold references (Python 2 compatible)

    def convert(node):
        if node:
            # Convert the left subtree
            convert(node.left)
            
            # Link the previous node (last[0]) with the current one (node)
            if last[0]:
                last[0].right = node
                node.left = last[0]
            else:
                first[0] = node
            
            last[0] = node  # Update last pointer
            
            # Convert the right subtree
            convert(node.right)

    convert(root)
    
    # Close the circular doubly linked list
    last[0].right = first[0]
    first[0].left = last[0]
    
    return first[0]

# Helper function to print the circular doubly linked list
def print_doubly_linked_list(head):
    if not head:
        return
    current = head
    while True:
        # Python 2 & 3 compatible print
        sys.stdout.write(str(current.val) + " <-> ")  # Works in both versions
        current = current.right
        if current == head:
            break
    print()

# Example usage
if __name__ == "__main__":
    # Construct the tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    # Convert the tree to a circular doubly linked list
    head = tree_to_doubly_list(root)

    # Print the circular doubly linked list
    print_doubly_linked_list(head)
