class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def printReversedList(head):
    stack = []
    current = head
    while current:
        stack.append(current.value)
        current = current.next
    while stack:
        print(stack.pop())

# Example usage:
# Creating a linked list 1 -> 2 -> 3
head = ListNode(1, ListNode(2, ListNode(3)))
printReversedList(head)