# Problem Statement
# Given a string S, remove all duplicate characters while keeping the first occurrence of each character and preserving their original order.

# Input Format
# A single string S.

# Output Format
# Print the resulting string after removing duplicate characters.

# Constraints
# 1 ≤ len(S) ≤ 10^5
# S contains lowercase English letters.

# Example Input
# programming
# Example Output
# progamin

# Your analysis
# Use the same format:
# Input:
# Goal:
# Important clue:
# Brute force:
# Brute force complexity:
# Constraint check:
# Repeated work:
# Pattern / Algorithm:
# Why?

def remove_duplicates(s):
    seen =set()
    result = []

    for ch in s:
        if ch not in seen:
            result.append(ch)
            seen.add(ch)

    return ''.join(result)

s = "programming"
print(remove_duplicates(s))  # Output: progamin