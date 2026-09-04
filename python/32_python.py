# A string S consists only of the characters ( and ).
# A valid string follows these rules:
# Every ( must eventually be matched with a ).
# A ) cannot appear before its corresponding (.
# All pairs must be completely matched by the end of the string.
# Determine whether the given string is valid.

# Input Format
# A single string S.

# Output Format
# Print YES if the string is valid.
# Otherwise, print NO.

# Constraints
# 1 ≤ |S| ≤ 10^5
# S contains only ( and ).

# Example 1
# Input
# (()())
# Output
# YES

# Example 2
# Input
# ())(
# Output
# NO

# Example 3
# Input
# ((())
# Output
# NO

def is_valid_parentheses(s):
    stack = []

    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return "NO"
            stack.pop()
    
    return "YES" if not stack else "NO"

        

s = "())()("
print(is_valid_parentheses(s))  # Output: YES