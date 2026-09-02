# Problem Statement
# Given an array of positive integers and an integer K, find the length of the smallest contiguous subarray whose sum is greater than or equal to K.
# If no such subarray exists, return 0.

# Input Format
# First line: integer N
# Second line: N integers
# Third line: integer K

# Output Format
# Print the minimum length of a contiguous subarray whose sum is at least K.

# Constraints
# 1 ≤ N ≤ 10^5
# 1 ≤ arr[i] ≤ 10^4
# 1 ≤ K ≤ 10^9

# Example Input
# N = 6
# arr = [2, 3, 1, 2, 4, 3]
# K = 7

# Example Output
# 2

# Your analysis
# Don't code yet. Answer:
# 1. Input:
# 2. Goal:
# 3. Important clue:
# 4. Brute force:
# 5. Brute force complexity:
# 6. Constraint check:
# 7. Repeated work:
# 8. Pattern / Algorithm:
# 9. Why?

def min_subarray_length(arr, k):
    min_length = float('inf')
    current_sum = 0
    start = 0 

    for end in range(len(arr)):
        current_sum += arr[end]

        while current_sum >= k:
            current_length = end - start + 1
            min_length = min(min_length, current_length) 
            current_sum -= arr[start]
            start += 1

    if min_length == float('inf'):
        return 0
    return min_length

arr = [2, 3, 1, 2, 4, 3]
k = 7
print(min_subarray_length(arr, k))  # Output: 2
