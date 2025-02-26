def zero_matrix(matrix):
    if not matrix or not matrix[0]:
        return matrix

    rows = len(matrix)
    cols = len(matrix[0])
    row_flags = [False] * rows
    col_flags = [False] * cols

    # First pass to find all rows and columns that need to be updated
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]:
                row_flags[i] = True
                col_flags[j] = True

    # Second pass to update the matrix
    for i in range(rows):
        for j in range(cols):
            if row_flags[i] or col_flags[j]:
                matrix[i][j] = True

    return matrix

# Example usage
matrix = [
    [True, False, False],
    [False, False, False],
    [False, False, False]
]

updated_matrix = zero_matrix(matrix)
for row in updated_matrix:
    print(row)