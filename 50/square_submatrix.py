def largest_square_submatrix(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    max_side = 0

    # Create a DP table to store the size of the largest square submatrix ending at each cell
    dp = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_side = max(max_side, dp[i][j])

    return max_side

# Example usage:
matrix = [
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0]
]

print(largest_square_submatrix(matrix))  # Output: 2