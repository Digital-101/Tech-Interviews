def longest_common_substring(str1, str2):
    m = len(str1)
    n = len(str2)
    max_len = 0
    ending_index = m

    # Create a 2D array to store lengths of longest common suffixes of substrings
    length = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the length array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                length[i][j] = length[i - 1][j - 1] + 1
                if length[i][j] > max_len:
                    max_len = length[i][j]
                    ending_index = i
            else:
                length[i][j] = 0

    # The longest common substring is from ending_index - max_len to ending_index
    return str1[ending_index - max_len: ending_index]

# Example usage
print(longest_common_substring("ABAB", "BABA"))  # Output: "ABA"