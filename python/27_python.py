# Problem Statement
# Given a string S and a character C, count how many times C occurs in S.

# Input Format
# First line: string S
# Second line: character C

# Output Format
# Print the number of times C occurs in S.

# Constraints
# 1 ≤ len(S) ≤ 10^5
# S contains lowercase English letters.
# C is a lowercase English letter.

# Example Input
# programming
# g
# Example Output
# 2

# Your turn
# Analyze it using:
# Input:
# Goal:
# Important clue:
# Brute force:
# Brute force complexity:
# Constraint check:
# Repeated work:
# Pattern / Algorithm:
# Why?

def count_character_occurrences(arr, c):
    count = 0
    for ch in arr:
        if ch == c:
            count += 1
    return count

arr = "programming"
c = 'g'
print(count_character_occurrences(arr, c))  # Output: 2