import heapq

def merge_k_arrays(arrays):
    min_heap = []
    for i, array in enumerate(arrays):
        if array:
            heapq.heappush(min_heap, (array[0], i, 0))

    result = []
    while min_heap:
        val, list_idx, element_idx = heapq.heappop(min_heap)
        result.append(val)
        if element_idx + 1 < len(arrays[list_idx]):
            next_tuple = (arrays[list_idx][element_idx + 1], list_idx, element_idx + 1)
            heapq.heappush(min_heap, next_tuple)

    return result

# Example usage:
arrays = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
print(merge_k_arrays(arrays))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]