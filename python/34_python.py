# Problem Statement
# You are given a string S containing only three types of brackets:
# ( ) [ ]
# Determine whether the brackets are properly matched and correctly nested.
# A bracket is valid only when its closing bracket matches the most recently opened unmatched bracket.

# Input Format
# A single string S.

# Output Format
# Print YES if the string is valid.
# Otherwise, print NO.

# Constraints
# 1 ≤ |S| ≤ 10^5
# S contains only (, ), [, ].

# Example 1
# Input
# ([()])
# Output
# YES

# Example 2
# Input
# ([)]
# Output
# NO

# Example 3
# Input
# (([]))
# Output
# YES

# Example 4
# Input
# ([]
# Output
# NO

def is_valid_brackets(s):
    stack = []
    bracket_pairs = {')':'(', ']':'['}

    for ch in s:
        if ch in '([':
            stack.append(ch)
        else:
            if not stack or stack.pop() != bracket_pairs[ch]:
                return "NO"
    return "YES" if not stack else "NO"

s = "([()])"
print(is_valid_brackets(s))  # Output: YES
          
