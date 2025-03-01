def gray(a, b):
    # XOR the two numbers to find differing bits
    xor = a ^ b
    # Check if the result is a power of 2 (only one bit is set)
    return (xor & (xor - 1)) == 0 and xor != 0

# Test cases
print(gray(0, 1))  # True
print(gray(1, 2))  # False