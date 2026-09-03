# Given a string S, determine whether the string contains only unique characters.

# Return "YES" if no character appears more than once. Otherwise, return "NO".

# Input Format
# A single string S.

# Output Format
# Print "YES" if all characters are unique, otherwise print "NO".

# Constraints
# 1 ≤ len(S) ≤ 10^5
# S contains lowercase English letters.

# Example Input
# abcdef
# Example Output
# YES

def has_unique_characters(s):
    seen = set(s)

    if len(seen) == len(s):
        return "YES"
    else:
        return "NO"

s = "abcdef"
print(has_unique_characters(s))  # Output: YES