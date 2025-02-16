def find_median_sorted_arrays(arr1, arr2):
    # Merge the two arrays
    merged_array = sorted(arr1 + arr2)
    
    # Find the length of the merged array
    n = len(merged_array)
    
    # If the length is odd, return the middle element
    if n % 2 == 1:
        return merged_array[n // 2]
    # If the length is even, return the average of the two middle elements
    else:
        return (merged_array[(n // 2) - 1] + merged_array[n // 2]) // 2

# Example usage
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
print(find_median_sorted_arrays(arr1, arr2))  # Output: 3.5