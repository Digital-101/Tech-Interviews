def swap(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

# Example usage:
x = 5
y = 10
print("before swap:", x, y)
x, y = swap(x, y)
print("Swapped values:", x, y)