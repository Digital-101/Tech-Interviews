def mod(byte_list, b):
    # Convert the list of bytes to a single integer
    big_int = 0
    for byte in byte_list:
        big_int = (big_int << 8) | byte
    
    # Return the result of big_int % b
    return big_int % b

# Example usage
byte_list = [0x03, 0xED]
b = 10
print(mod(byte_list, b))  # Output: 5