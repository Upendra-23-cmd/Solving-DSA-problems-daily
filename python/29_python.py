# Problem Statement
# Given a string S, find the first character that occurs more than once.
# If no character is repeated, return -1.

# Input Format
# A single string S.

# Output Format
# Print the first character that appears more than once, according to its position in the original string.

# Constraints
# 1 ≤ len(S) ≤ 10^5
# S contains lowercase English letters.

# Example Input
# abca
# Example Output
# a

def first_repeated_character(s):
    seen = {}
    count = 0

    for ch in s:
        seen[ch] = seen.get(ch, 0) + 1
    for ch in s:
        if seen[ch] > 1:
            return ch

    return -1

s = "abca"
print(first_repeated_character(s))  # Output: a 