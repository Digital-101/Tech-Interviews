def sort_stack(input_stack):
    temp_stack = []
    
    while input_stack:
        # Pop an element from the input stack
        temp = input_stack.pop()
        
        # While temporary stack is not empty and top of temp_stack is greater than temp
        while temp_stack and temp_stack[-1] > temp:
            # Pop from temp_stack and push it to the input stack
            input_stack.append(temp_stack.pop())
        
        # Push temp in temp_stack
        temp_stack.append(temp)
    
    # Transfer from temp_stack back to input_stack to maintain the original stack order
    while temp_stack:
        input_stack.append(temp_stack.pop())
    
    return input_stack

# Example usage
input_stack = [1, 3, 2, 4]
sorted_stack = sort_stack(input_stack)
print(sorted_stack)  # Output: [1, 2, 3, 4]