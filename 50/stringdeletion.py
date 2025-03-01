def min_deletions_to_form_word(dictionary, query):
    # Convert dictionary list to a set for faster lookup
    dictionary_set = set(dictionary)
    
    # Helper function to check if a word can be formed by deleting characters
    def can_form_word(word):
        if word in dictionary_set:
            return True
        return False
    
    # Recursive function to find the minimum deletions
    def find_min_deletions(word):
        if can_form_word(word):
            return 0
        min_deletions = float('inf')
        for i in range(len(word)):
            new_word = word[:i] + word[i+1:]
            deletions = 1 + find_min_deletions(new_word)
            min_deletions = min(min_deletions, deletions)
        return min_deletions
    
    return find_min_deletions(query)

# Example usage
dictionary = ["a", "aa", "aaa"]
query = "abc"
print(min_deletions_to_form_word(dictionary, query))  # Output: 2