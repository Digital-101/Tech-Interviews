class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def split_linked_list(head):
    if not head or not head.next:
        return head, None

    slow = head
    fast = head
    prev = None

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    if prev:
        prev.next = None

    return head, slow

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# Example usage
if __name__ == "__main__":
    # Creating a linked list 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Splitting the linked list
    first_half, second_half = split_linked_list(head)

    # Printing the two halves
    print("First half:")
    print_linked_list(first_half)
    print("Second half:")
    print_linked_list(second_half)