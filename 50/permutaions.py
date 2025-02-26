from itertools import permutations

def get_permutations(lst):
    return list(permutations(lst))

# Example usage
example_list = [1, 2, 3]
result = get_permutations(example_list)
for perm in result:
    print(perm)