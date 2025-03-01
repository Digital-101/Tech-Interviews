def rotate_bits(n, k, bits=32):
    # Ensure k is within the range of bits
    k = k % bits
    # Perform the rotation
    return ((n << k) & ((1 << bits) - 1)) | (n >> (bits - k))

# Test cases
print(hex(rotate_bits(0xFFFF0000, 8)))  # Output: 0x00FFFF00
print(hex(rotate_bits(0x13579BDF, 12)))  # Output: 0xBDF13579
print(bin(rotate_bits(0b10110011100011110000111110000000, 17)))  # Output: 0b00011111000000010110011100011110