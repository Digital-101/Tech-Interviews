def count_ones_in_binary(n):
    """
    This function takes an integer n and returns the number of ones in its binary representation.
    
    :param n: Integer input
    :return: Number of ones in the binary representation of n
    """
    # Convert the number to binary and count the number of '1's
    return bin(n).count('1')

# Example usage:
if __name__ == "__main__":
    number = 29  # Example number
    print("The number of ones in the binary representation of {} is {}".format(number, count_ones_in_binary(number)))
