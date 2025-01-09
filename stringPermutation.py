def permute(s, answer=""):
    if len(s) == 0:
        print(answer)  # Base case: print the permutation
        return
    
    for i in range(len(s)):
        char = s[i]  # Pick the current character
        remaining = s[:i] + s[i+1:]  # Remove the picked character
        permute(remaining, answer + char)  # Recursive call

# Example usage
string = "abc"
print(f"Permutations of '{string}':")
permute(string)
