# Problem Statement
# A string S contains only the characters (, ), [, ], {, and }.
# Determine whether the string represents a valid sequence of brackets.

# A sequence is valid when:
# Every opening bracket has a corresponding closing bracket.
# A closing bracket must correspond to the most recently opened bracket that has not yet been closed.
# Brackets may be nested inside one another.

# Input Format
# A single string S.
# Output Format
# Print YES if the sequence is valid; otherwise print NO.

# Constraints
# 1 ≤ |S| ≤ 10^5

# Examples
# Input
# {[()]}

# Output
# YES

# Input
# {[(])}
# Output
# NO
# Input
# ([{}])
# Output
# YES
# Input
# ((]
# Output
# NO

# 🎯 Your task — DON'T CODE YET
# Analyze it using exactly:
# 1. Input:
# 2. Goal:
# 3. Important clue:
# 4. Brute force:
# 5. Brute force complexity:
# 6. Constraint check:
# 7. Repeated work:
# 8. Pattern / Algorithm:
# 9. Why?

def pair_brackets(s):
    stack = []
    bracket_pairs = {')':'(',']':'[','}':'{'}

    for ch in s:
        if ch in '([{':
            stack.append(ch)
        else:
            if not stack or stack.pop() != bracket_pairs[ch]:
                return "NO"
    return "YES" if not stack else "NO"

s = "{[()]}"
print(pair_brackets(s))  # Output: YES