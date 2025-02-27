from collections import defaultdict, deque

def find_build_order(num_packages, dependencies):
    # Create a graph and a degree of dependencies (in-degree) array
    graph = defaultdict(list)
    in_degree = [0] * num_packages

    # Build the graph and fill the in-degree array
    for package, dep in dependencies:
        graph[dep].append(package)
        in_degree[package] += 1

    # Initialize a queue with all packages that have no dependencies (in-degree 0)
    queue = deque([i for i in range(num_packages) if in_degree[i] == 0])
    build_order = []

    while queue:
        current = queue.popleft()
        build_order.append(current)

        # Decrease the in-degree of the current package's neighbors
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            # If in-degree becomes 0, add it to the queue
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If build_order contains all packages, return it; otherwise, return an error (cycle detected)
    if len(build_order) == num_packages:
        return build_order
    else:
        return "Error: Cycle detected, no valid build order exists."

# Example usage
num_packages = 5
dependencies = [(1, 0), (2, 0), (3, 1), (3, 2), (4, 3)]
print(find_build_order(num_packages, dependencies))