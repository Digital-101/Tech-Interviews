def mergeArrays(A, B):
    # Get the lengths of A and B
    lenA = len(A) - len(B)
    lenB = len(B)
    
    # Pointers for A, B, and the merged array
    i = lenA - 1
    j = lenB - 1
    k = lenA + lenB - 1
    
    # Merge A and B from the end
    while i >= 0 and j >= 0:
        if A[i] > B[j]:
            A[k] = A[i]
            i -= 1
        else:
            A[k] = B[j]
            j -= 1
        k -= 1
    
    # Copy any remaining elements from B
    while j >= 0:
        A[k] = B[j]
        j -= 1
        k -= 1

# Example usage
A = [1, 3, 5, 0, 0, 0]
B = [2, 4, 6]
mergeArrays(A, B)
print(A)  # Output: [1, 2, 3, 4, 5, 6]