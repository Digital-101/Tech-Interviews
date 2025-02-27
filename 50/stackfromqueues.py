from Queue import Queue

class StackFromQueues:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, x):
        self.queue1.put(x)

    def pop(self):
        if self.queue1.empty():
            return None
        
        while self.queue1.qsize() > 1:
            self.queue2.put(self.queue1.get())
        
        popped_element = self.queue1.get()
        
        self.queue1, self.queue2 = self.queue2, self.queue1
        
        return popped_element

    def top(self):
        if self.queue1.empty():
            return None
        
        while self.queue1.qsize() > 1:
            self.queue2.put(self.queue1.get())
        
        top_element = self.queue1.get()
        self.queue2.put(top_element)
        
        self.queue1, self.queue2 = self.queue2, self.queue1
        
        return top_element

    def empty(self):
        return self.queue1.empty()

# Example usage:
stack = StackFromQueues()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # Output: 3
print(stack.top())  # Output: 2
print(stack.empty())  # Output: False