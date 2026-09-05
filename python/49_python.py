# Problem
# Given an array of integers, find the maximum difference arr[j] - arr[i] such that:
# i < j
# If no positive difference exists, return 0.

# Input Format
# N
# arr[0] arr[1] ... arr[N-1]

# Output Format
# Print the maximum possible difference.

# Constraints
# 1 ≤ N ≤ 10^5
# -10^9 ≤ arr[i] ≤ 10^9

# Example 1
# 6
# 7 1 5 3 6 4
# Output:
# 5
# Because:
# 6 - 1 = 5
# Example 2
# 5
# 9 7 4 3 1
# Output:
# 0
# There is no positive difference.
# Example 3
# 6
# 10 2 8 1 9 4
# Output:
# 8
# Because:
# 9 - 1 = 8

# Your analysis
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

def max_difference(arr):
    current_min = arr[0]
    max_diff = 0

    for i in range(len(arr)):
        current_diff = arr[i]- current_min
        max_diff = max(max_diff, current_diff)
        current_min = min(current_min, arr[i])
    return max_diff

arr = [7, 1, 5, 3, 6, 4]
print(max_difference(arr))  # Output: 5
