class Autocomplete:
    def __init__(self, words):
        self.words = words

    def find_words_with_prefix(self, prefix):
        return [word for word in self.words if word.startswith(prefix)]

# Example usage:
words = {"abc", "acd", "bcd", "def", "a", "aba"}
autocomplete = Autocomplete(words)
print(autocomplete.find_words_with_prefix("a"))  # Output: ['abc', 'acd', 'a', 'aba']
print(autocomplete.find_words_with_prefix("b"))  # Output: ['bcd']