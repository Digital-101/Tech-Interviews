def isAnagram(s1, s2):
    # Convert both strings to lowercase to handle case insensitivity
    s1 = s1.lower()
    s2 = s2.lower()
    
    # Check if the lengths of the strings are different
    if len(s1) != len(s2):
        return False
    
    # Sort the characters of both strings and compare
    return sorted(s1) == sorted(s2)

# Test cases
print(isAnagram("", ""))  # True
print(isAnagram("A", "A"))  # True
print(isAnagram("A", "B"))  # False
print(isAnagram("ab", "ba"))  # True
print(isAnagram("AB", "ab"))  # True