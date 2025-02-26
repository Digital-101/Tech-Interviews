def contains(matrix, x):
    if not matrix:
        return False

    rows = len(matrix)
    cols = len(matrix[0])

    # Start from the top-right corner
    row = 0
    col = cols - 1

    while row < rows and col >= 0:
        if matrix[row][col] == x:
            return True
        elif matrix[row][col] > x:
            col -= 1
        else:
            row += 1

    return False

# Example usage:
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
x = 7
print(contains(matrix, x))  # Output: True