# Problem
# Given an array of integers and an integer K, find the minimum length of a contiguous subarray whose sum is greater than or equal to K.
# If no such subarray exists, return 0.

# Input Format
# N
# arr[0] arr[1] ... arr[N-1]
# K

# Output Format
# Print the minimum length.

# Constraints
# 1 ≤ N ≤ 10^5
# 1 ≤ arr[i] ≤ 10^9
# 1 ≤ K ≤ 10^14

# Example 1
# 6
# 2 3 1 2 4 3
# 7
# Output:
# 2
# Because:
# 4 + 3 = 7
# Example 2
# 5
# 1 1 1 1 1
# 11
# Output:
# 0
# Example 3
# 6
# 1 4 4 2 5 1
# 8
# Output:
# 2
# Because:
# 4 + 4 = 8

# Input:
# Goal:
# Important clue:
# Brute force:
# Brute force complexity:
# Constraint check:
# Repeated work:
# Pattern / Algorithm:
# Why?

def min_subarray_length(arr, k):
    min_length = float('inf')
    current_sum = 0
    start = 0

    for end in range(len(arr)):
        current_sum += arr[end]

        while current_sum >= k:
            current_length = end -start + 1
            min_length = min(min_length, current_length)
            current_sum -= arr[start]
            start += 1

    if min_length == float('inf'):
        return 0
    return min_length

arr = [2, 3, 1, 2, 4, 3]
k = 7
print(min_subarray_length(arr, k))  # Output: 2