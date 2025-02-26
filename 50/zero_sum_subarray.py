def zero_sum_subarray(arr):
    sum_map = {}
    current_sum = 0

    for i, num in enumerate(arr):
        current_sum += num

        if current_sum == 0:
            return arr[:i + 1]

        if current_sum in sum_map:
            return arr[sum_map[current_sum] + 1:i + 1]

        sum_map[current_sum] = i

    return None

# Example usage
print(zero_sum_subarray([1, 2, -5, 1, 2, -1]))  # Output: [2, -5, 1, 2]