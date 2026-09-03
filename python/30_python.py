# Problem Statement
# Given a string S, reverse the order of its characters and return the reversed string.

# Input Format
# A single string S.

# Output Format
# Print the reversed string.

# Constraints
# 1 ≤ len(S) ≤ 10^5
# S contains lowercase English letters.

# Example Input
# hello
# Example Output
# olleh

def reverse_string(s):
    first = 0
    last = len(s) - 1

    while first < last:
        s[first], s[last] = s[last], s[first]
        first += 1
        last -= 1

    return ''.join(s)

s = "hello"
print(reverse_string(list(s)))  # Output: olleh
