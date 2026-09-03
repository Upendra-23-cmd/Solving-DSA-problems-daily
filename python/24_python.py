# Problem Statement
# Given two strings S and T, determine whether they contain the same characters with the same frequencies, regardless of their order.
# Return "YES" if they do, otherwise return "NO".

# Input Format
# Two strings S and T.

# Output Format
# Print "YES" if they contain the same characters with the same frequencies, otherwise print "NO".

# Constraints
# 1 ≤ len(S), len(T) ≤ 10^5

# Strings contain lowercase English letters.
# Example Input
# listen
# silent
# Example Output
# YES

def are_same(s,t):
    
    if len(s) != len(t):
        return "NO"
    
    char_count_s = {}
    char_count_t = {}

    for ch in s:
        char_count_s[ch] = char_count_s.get(ch, 0) + 1
    for ch in t:
        char_count_t[ch] = char_count_t.get(ch, 0) + 1
    
    if char_count_s == char_count_t:
        return "YES"
    else:
        return "NO"
    
s = "listen"
t = "silent"
print(are_same(s, t))  # Output: YES
