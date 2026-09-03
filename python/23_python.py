# Problem Statement
# Given a string S, determine whether it reads the same from left to right and right to left.
# If it is the same, return "YES", otherwise return "NO".

# Input Format
# A single string S.

# Output Format
# Print "YES" if the string is a palindrome, otherwise print "NO".

# Constraints
# 1 ≤ len(S) ≤ 10^5
# S contains lowercase English letters.

# Example Input
# madam
# Example Output
# YES

# Your analysis
# Answer in this exact format:
# Input:
# Goal:
# Important clue:
# Brute force:
# Brute force complexity:
# Constraint check:
# Repeated work:
# Pattern / Algorithm:
# Why?

def is_palindrome(s):
    left = 0
    right = len(s)-1

    while left < right:
        if s[left] != s[right]:
            return "NO"
        left += 1
        right -= 1
    return "YES"

s = "madam"
print(is_palindrome(s))  # Output: YES