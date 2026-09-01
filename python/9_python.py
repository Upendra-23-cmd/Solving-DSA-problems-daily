# Question 10: Count Pairs With a Given Difference
# Problem Statement
# Given an array of integers and an integer K, find the number of unique pairs of elements whose absolute difference is exactly K.
# Each pair should be counted only once.

# For example, (2, 5) and (5, 2) are considered the same pair.

# Input Format
# First line: Integer N
# Second line: N space-separated integers
# Third line: Integer K

# Output Format
# Print the number of unique pairs whose absolute difference is K.

# Constraints
# 2 ≤ N ≤ 10^5
# 0 ≤ K ≤ 10^9
# -10^9 ≤ arr[i] ≤ 10^9

# Example Input
# 6
# 1 5 3 4 2 6
# 2
# Example Output
# 4

# The valid pairs are:
# (1, 3)
# (3, 5)
# (2, 4)
# (4, 6)

# Now analyze it without looking for the solution yet.
# Answer exactly:
# Input:
# Goal:
# Important clue:
# Brute force:
# Brute force complexity:
# Constraint check:
# Repeated work:
# Pattern / Algorithm:
# Why?

def count_pairs_with_difference(arr, k):
    num_set = set(arr)
    count = 0

    for num in num_set:
        if num +k in num_set:
            count += 1
    
    return count

arr = [1, 5, 3, 4, 2, 6]
k = 2
print(count_pairs_with_difference(arr, k))  # Output: 4