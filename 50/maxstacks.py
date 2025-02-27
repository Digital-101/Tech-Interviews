class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.max_stack or value >= self.max_stack[-1]:
            self.max_stack.append(value)

    def pop(self):
        if not self.stack:
            return None
        value = self.stack.pop()
        if value == self.max_stack[-1]:
            self.max_stack.pop()
        return value

    def max(self):
        if not self.max_stack:
            return None
        return self.max_stack[-1]

# Example usage:
max_stack = MaxStack()
max_stack.push(1)
print(max_stack.max())  # Output: 1
max_stack.push(2)
print(max_stack.max())  # Output: 2
max_stack.push(1)
print(max_stack.max())  # Output: 2
print(max_stack.pop())  # Output: 1
print(max_stack.max())  # Output: 2
print(max_stack.pop())  # Output: 2
print(max_stack.max())  # Output: 1