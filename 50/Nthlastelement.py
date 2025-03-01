class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def nth_to_last(head: ListNode, n: int) -> ListNode:
    # Initialize two pointers
    first = head
    second = head
    
    # Move the first pointer n steps ahead
    for _ in range(n):
        if first is None:
            return None  # n is larger than the length of the list
        first = first.next
    
    # Move both pointers until the first pointer reaches the end
    while first is not None:
        first = first.next
        second = second.next
    
    return second

# Helper function to create a linked list from a list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = 2
    head = create_linked_list(arr)
    result = nth_to_last(head, n)
    if result:
        print(f"The {n}th-to-last element is {result.value}")
    else:
        print("The list is shorter than n elements.")