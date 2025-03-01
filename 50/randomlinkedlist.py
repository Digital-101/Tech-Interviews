class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def clone_linked_list(head):
    if not head:
        return None

    # Step 1: Create a new node for each node and insert it right next to the original node.
    current = head
    while current:
        new_node = Node(current.val, current.next)
        current.next = new_node
        current = new_node.next

    # Step 2: Assign random pointers for the new nodes.
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next

    # Step 3: Separate the original list and the cloned list.
    current = head
    new_head = head.next
    while current:
        clone = current.next
        current.next = clone.next
        if clone.next:
            clone.next = clone.next.next
        current = current.next

    return new_head

# Helper function to print the list for testing
def print_list(head):
    current = head
    while current:
        random_val = current.random.val if current.random else None
        print('Node value: {}, Random points to: {}'.format(current.val, random_val))
        current = current.next

# Example usage
if __name__ == "__main__":
    # Creating the linked list 1 -> 2 -> 3 -> 4 -> null with random pointers
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node1.random = node3
    node2.random = node1
    node3.random = node3
    node4.random = node2

    print("Original list:")
    print_list(node1)

    cloned_head = clone_linked_list(node1)

    print("\nCloned list:")
    print_list(cloned_head)