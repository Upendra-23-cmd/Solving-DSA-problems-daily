# Problem Statement
# A text editor stores the characters entered by a user. The user can perform two operations:
# Type a character — adds it to the end of the current text.
# Undo — removes the most recently added character.

# You are given a sequence of operations. Starting with an empty string, determine the final text after performing all operations.
# Input Format
# First line: integer N, the number of operations.
# The next N lines contain one operation:
# TYPE c — add character c
# UNDO — remove the most recently added character, if one exists.

# Output Format
# Print the final text.

# Constraints
# 1 ≤ N ≤ 10^5
# c is a lowercase English letter

# Example
# Input
# 7
# TYPE a
# TYPE b
# TYPE c
# UNDO
# TYPE d
# UNDO
# TYPE e
# Output
# abe
# Another Example
# Input
# 6
# TYPE a
# TYPE b
# UNDO
# UNDO
# UNDO
# TYPE c
# Output
# c

def final_text( n):

    stack = []
    for i in range(n):
        inputs = input().split()
        if inputs[0] == "TYPE":
            stack.append(inputs[1])
        else:
            if stack:
                stack.pop()

    return ''.join(stack)

n = int(input())
print(final_text(n))  # Output: abe        