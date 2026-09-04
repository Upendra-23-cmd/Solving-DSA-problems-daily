# Given a string S, count how many words it contains.
# Words are separated by one or more spaces.

# Input Format
# A single string S.

# Output Format
# Print the number of words in the string.

# Constraints
# 1 ≤ len(S) ≤ 10^5
# S contains lowercase English letters and spaces.

# Example Input
# I love programming
# Example Output
# 3

# This is a traversal problem. We can traverse the string and count the number of words by checking for spaces., travesal means going through once

def count_words(s):
    count = 0
    in_word = False

    for ch in s:
        if ch != ' ' and not in_word:
            count += 1
            in_word = True
        elif ch == ' ':
            in_word = False
        
    return count

s = "I love programming"
print(count_words(s))  # Output: 3

