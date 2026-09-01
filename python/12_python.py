# Problem Statement
# Given an array of integers, find the maximum possible sum of a contiguous subarray.
# A contiguous subarray means the elements must be next to each other.

# You only need to return the maximum sum.
# Input Format
# First line: Integer N
# Second line: N space-separated integers

# Output Format
# Print the maximum subarray sum.

# Constraints
# 1 ≤ N ≤ 10^5
# -10^4 ≤ arr[i] ≤ 10^4

# Example Input
# 8
# -2 1 -3 4 -1 2 1 -5
# Example Output
# 6

# Explanation
# The subarray:
# [4, -1, 2, 1]
# has sum:
# 4 + (-1) + 2 + 1 = 6
# and no other contiguous subarray has a larger sum.

def max_subarray_sum(arr):
    max_sum = arr[0]
    current_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum

arr = [-2, 1, -3, 4, -1, 2, 1, -5]
print(max_subarray_sum(arr))  # Output: 6