# Question 8: Subarray Sum Equals K
# Problem Statement
# Given an array of N integers and an integer K, find the number of continuous subarrays whose sum is exactly equal to K.
# A subarray is a continuous part of the array.

# Input Format
# First line: Integer N
# Second line: N space-separated integers
# Third line: Integer K

# Output Format
# Print the number of continuous subarrays whose sum equals K.

# Constraints
# 1 ≤ N ≤ 10^5
# -10^9 ≤ arr[i] ≤ 10^9
# -10^9 ≤ K ≤ 10^9

# Example Input
# 5
# 1 1 1 2 1
# 3

# Example Output
# 3

def subarray_sum_equals_k(arr, k):
    prefix_sum_count = {0: 1}

    prefix_sum = 0
    count = 0

    for num in arr:
        prefix_sum += num
        if prefix_sum - k in prefix_sum_count:
            count += prefix_sum_count[prefix_sum - k]
        prefix_sum_count[prefix_sum] = prefix_sum_count.get(prefix_sum, 0) + 1

    return count

arr = [1, 1, 1, 2, 1,1,1]
k = 3
print(subarray_sum_equals_k(arr, k))  # Output: 3