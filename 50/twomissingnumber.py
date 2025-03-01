def find_two_missing_numbers(arr):
    n = len(arr) + 2
    total_sum = n * (n + 1) / 2
    arr_sum = sum(arr)
    pivot = (total_sum - arr_sum) / 2

    total_left_xor = 0
    arr_left_xor = 0
    total_right_xor = 0
    arr_right_xor = 0

    for i in range(1, int(pivot) + 1):
        total_left_xor ^= i
    for i in range(int(pivot) + 1, n + 1):
        total_right_xor ^= i

    for num in arr:
        if num <= pivot:
            arr_left_xor ^= num
        else:
            arr_right_xor ^= num

    missing1 = total_left_xor ^ arr_left_xor
    missing2 = total_right_xor ^ arr_right_xor

    return missing1, missing2

# Example usage
arr = [4, 2, 3]
print(find_two_missing_numbers(arr))  # Output: (1, 5)