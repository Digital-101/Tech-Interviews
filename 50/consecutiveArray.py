def consecutive(arr):
    if not arr:
        return 0, []

    num_set = set(arr)
    longest_streak = 0
    best_sequence = []

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            current_sequence = [current_num]

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
                current_sequence.append(current_num)

            if current_streak > longest_streak:
                longest_streak = current_streak
                best_sequence = current_sequence

    return longest_streak, best_sequence

# Test cases
print(consecutive([4, 2, 1, 6, 5]))  # Output: (3, [4, 5, 6])
print(consecutive([5, 5, 3, 1]))     # Output: (1, [1], [3], or [5])