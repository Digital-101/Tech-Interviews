from collections import Counter

def kthMostFrequent(strings, k):
    if not strings or k < 0:
        return None
    
    frequency = Counter(strings)
    sorted_strings = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    
    if k >= len(sorted_strings):
        return None
    
    return sorted_strings[k][0]

# Test cases
print(kthMostFrequent(["a", "b", "c", "a", "b", "a"], 0))  # Output: "a"
print(kthMostFrequent(["a", "b", "c", "a", "b", "a"], 1))  # Output: "b"
print(kthMostFrequent(["a", "b", "c", "a", "b", "a"], 2))  # Output: "c"
print(kthMostFrequent(["a", "b", "c", "a", "b", "a"], 3))  # Output: None