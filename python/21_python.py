# Given an array of positive integers and an integer K, find the maximum sum of any contiguous subarray containing exactly K elements.

# Input Format
# First line: integer N
# Second line: N integers
# Third line: integer K

# Output Format
# Print the maximum sum.

# Constraints
# 1 ≤ K ≤ N ≤ 10^5
# 1 ≤ arr[i] ≤ 10^4

# Example Input
# N = 6
# arr = [2, 3, 1, 2, 4, 3]
# K = 3

# Example Output
# 9

# Because:
# [2, 3, 1] = 6
# [3, 1, 2] = 6
# [1, 2, 4] = 7
# [2, 4, 3] = 9  ← maximum

def max_sum_subarray_k(arr, k):
    max_sum = 0
    current_sum = sum(arr[:k])
    max_sum =current_sum

    for i in range(k, len(arr)):
        current_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, current_sum)
    
    return max_sum

arr = [2, 3, 1, 2, 4, 3]
k = 3
print(max_sum_subarray_k(arr, k))  # Output: 9