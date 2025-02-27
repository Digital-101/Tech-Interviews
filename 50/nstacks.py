class NStacks:
    def __init__(self, N, capacity):
        self.N = N
        self.capacity = capacity
        self.array = [None] * capacity
        self.tops = [-1] * N
        self.next_index = list(range(1, capacity)) + [-1]
        self.free = 0

    def is_full(self):
        return self.free == -1

    def is_empty(self, stack_num):
        return self.tops[stack_num] == -1

    def push(self, stack_num, value):
        if self.is_full():
            raise Exception("Stack Overflow")
        
        insert_at = self.free
        self.free = self.next_index[insert_at]
        self.next_index[insert_at] = self.tops[stack_num]
        self.tops[stack_num] = insert_at
        self.array[insert_at] = value

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception("Stack Underflow")
        
        top_index = self.tops[stack_num]
        self.tops[stack_num] = self.next_index[top_index]
        self.next_index[top_index] = self.free
        self.free = top_index
        return self.array[top_index]

# Example usage:
N = 3
capacity = 10
stacks = NStacks(N, capacity)
stacks.push(0, 10)
stacks.push(2, 11)
print(stacks.pop(0))  # Output: 10
print(stacks.pop(2))  # Output: 11