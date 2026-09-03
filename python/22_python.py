# Question 1
# Given a string, find the first character that appears only once in the string.
# If every character appears more than once, return -1.

# Input Format
# A single string S.

# Output Format
# Print the first non-repeating character, or -1.

# Constraints
# 1 ≤ len(S) ≤ 10^5
# S contains lowercase English letters

# Example Input
# S = "aabbcdde"
# Example Output
# c

# Because:
# a → 2 times
# b → 2 times
# c → 1 time  ← first unique
# d → 2 times
# e → 1 time

# Your analysis — don't code yet
# Use our same exam process:
# 1. Input:
# 2. Goal:
# 3. Important clue:
# 4. Brute force:
# 5. Brute force complexity:
# 6. Constraint check:
# 7. Repeated work:
# 8. Pattern / Algorithm:
# 9. Why?

def first_non_repeating_character(s):
    char_count = {}

    for ch in s:
        char_count[ch] = char_count.get(ch, 0)+ 1
    
    for ch in s:
        if char_count[ch] == 1:
            return ch
    return -1

s = "aabbcdde"
print(first_non_repeating_character(s))  # Output: c