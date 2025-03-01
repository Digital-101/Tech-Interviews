class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def dedup(head):
    if not head:
        return head

    seen = set()
    current = head
    seen.add(current.value)
    
    while current.next:
        if current.next.value in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.value)
            current = current.next
    
    return head

# Helper function to print the linked list
def print_list(head):
    current = head
    while current:
        if current.next:
            print(current.value, "->")  # Python 2.7 style print statement
        else:
            print(current.value)  # Print last value without arrow
        current = current.next

# Example usage
head = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1, None)))))  # Ensure the last node points to None
print("Original list:")
print_list(head)
head = dedup(head)
print("Deduplicated list:")
print_list(head)
