class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome(head):  # Removed type hints for Python 2 compatibility
    # Find the middle of the linked list
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half of the linked list
    prev = None
    while slow:
        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node

    # Compare the first and second half nodes
    left, right = head, prev
    while right:  # Only need to compare till right half
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True

# Example usage:
# Creating a linked list 1 -> 2 -> 1
head = ListNode(1, ListNode(2, ListNode(1)))
print(is_palindrome(head))  # Output: True

# Creating a linked list 1 -> 2 -> 3
head = ListNode(1, ListNode(2, ListNode(3)))
print(is_palindrome(head))  # Output: False
