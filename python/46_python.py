# Problem
# Given an array of integers, find the maximum sum of any contiguous subarray.
# A subarray must contain at least one element.

# Input Format
# N
# arr[0] arr[1] ... arr[N-1]

# Output Format
# Print the maximum possible subarray sum.

# Constraints
# 1 ≤ N ≤ 10^5
# -10^9 ≤ arr[i] ≤ 10^9

# Example 1
# 8
# -2 1 -3 4 -1 2 1 -5
# Output:
# 6
# Because:
# 4 + (-1) + 2 + 1 = 6
# Example 2
# 5
# -5 -2 -8 -1 -3
# Output:
# -1
# Example 3
# 6
# 3 -2 5 -1 4 -6
# Output:
# 9
# Because:
# 3 + (-2) + 5 + (-1) + 4 = 9

# Your analysis — don't write code yet
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

def max_subarray_sum(arr):
    max_sum = arr[0]
    current_sum =arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

arr = [-2, 1, -3, 4, -1, 2, 1, -5]
print(max_subarray_sum(arr))  # Output: 6

# NOTE : contigous subarray + maximum sum + whether to include previous sum or not =  Kadane's algorithm