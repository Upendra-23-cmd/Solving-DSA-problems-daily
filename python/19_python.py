# Problem Statement
# Given an array of integers, find the maximum difference between two elements such that the larger element appears after the smaller element.
# In other words, choose two indices i and j such that:
# i < j
# and maximize:
# arr[j] - arr[i]
# If no positive difference is possible, return 0.
# Input Format
# First line: an integer N
# Second line: N space-separated integers.
# Output Format
# Print the maximum possible difference.
# Constraints
# 2 ≤ N ≤ 10^5
# -10^9 ≤ arr[i] ≤ 10^9
# Example Input
# 6
# 7 1 5 3 6 4
# Example Output
# 5
# Now answer:
# 1. Input:
# 2. Goal:
# 3. Important clue:
# 4. Brute force:
# 5. Brute force complexity:
# 6. Constraint check:
# 7. Repeated work:
# 8. Pattern / Algorithm:
# 9. Why?

def max_difference(arr):
    current_min = arr[0]
    max_diff = 0

    for i in range(len(arr)):
        current_diff = arr[i] - current_min
        max_diff = max(max_diff, current_diff)
        current_min = min(current_min, arr[i])
    return max_diff

arr = [7, 1, 5, 3, 6, 4]
print(max_difference(arr))  # Output: 5
