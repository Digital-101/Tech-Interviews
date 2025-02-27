# -*- coding: utf-8 -*-
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def __repr__(self):
        return "Stack (Top → Bottom): " + " -> ".join(map(str, reversed(self.items)))

def insert_at_bottom(stack, item):
    """Inserts an element at the bottom of the stack."""
    if stack.is_empty():
        stack.push(item)
    else:
        temp = stack.pop()
        insert_at_bottom(stack, item)
        stack.push(temp)

def reverse_stack(stack):
    """Reverses a stack using recursion."""
    if not stack.is_empty():
        temp = stack.pop()
        reverse_stack(stack)
        insert_at_bottom(stack, temp)

# Example usage:
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    print("Original Stack:", stack)
    reverse_stack(stack)
    print("Reversed Stack:", stack)
