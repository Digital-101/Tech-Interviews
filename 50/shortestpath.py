from collections import deque

def shortestPath(graph, start, end):
    # Initialize the queue with the start node and the path taken so far
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current_node, path = queue.popleft()
        
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        # If we reached the end node, return the path
        if current_node == end:
            return path
        
        # Add all neighbors to the queue
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    
    # If no path is found, return an empty list
    return []

# Example usage
graph = {
    2: [5],
    5: [4],
    4: [3],
    3: []
}

print(shortestPath(graph, 2, 3))  # Output: [2, 5, 4, 3]