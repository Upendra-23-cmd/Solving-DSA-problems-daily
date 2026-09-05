# Problem
# You are given an array of integers and an integer K.
# Find the length of the longest contiguous subarray whose sum is exactly K.
# If no such subarray exists, return 0.

# Input
# N
# arr[0] arr[1] ... arr[N-1]
# K

# Constraints
# 1 ≤ N ≤ 10^5
# -10^9 ≤ arr[i] ≤ 10^9
# -10^14 ≤ K ≤ 10^14

# Example 1
# Input:
# 6
# 10 5 2 7 1 9
# 15

# Output:
# 4
# Explanation:
# 5 + 2 + 7 + 1 = 15
# So the longest valid subarray has length 4.
# Example 2
# Input:
# 5
# -1 -1 1 1 1
# 0

# Output:
# 4
# Example 3
# Input:
# 4
# 1 2 3 4
# 20

# Output:
# 0

# Write:
# 1. Input:
# 2. Goal:
# 3. Important clue:
# 4. Brute force:
# 5. Brute force complexity:
# 6. Constraint check:
# 7. Repeated work:
# 8. Pattern / Algorithm:
# 9. Why?

def first_continous_subarray(arr, k):
    prefix_sum = 0
    sum_index_map = {0: -1}
    max_length = 0

    for i in range(len(arr)):
        prefix_sum += arr[i]

        # to check if the prefix_sum - k exists in the map, if it does then we can find the length of the subarray
        if prefix_sum not in sum_index_map:
            sum_index_map[prefix_sum] = i

        # check if there is a prefix sum that when subtracted from the current prefix sum gives k
        if prefix_sum - k in sum_index_map:
            length = i - sum_index_map[prefix_sum - k]
            max_length = max(max_length, length)
        
    return max_length

arr = [10, 5, 2, 7, 1, 9]
k = 15
print(first_continous_subarray(arr, k))  # Output: 4

# Especially when the question asks things like:
# Sum of elements from index L to R
# Sum of every subarray
# Find a subarray with a particular sum
# Count subarrays whose sum is K
# Find whether a continuous subarray has sum K
# Multiple range-sum queries

# | Question clue                            | Think                              |
# | ---------------------------------------- | ---------------------------------- |
# | Repeated range sums                      | **Prefix Sum**                     |
# | Sum from `L` to `R`                      | **Prefix Sum**                     |
# | Many sum queries                         | **Prefix Sum**                     |
# | Count subarrays with sum `K`             | **Prefix Sum + HashMap**           |
# | Find subarray with sum `K` and negatives | **Prefix Sum + HashMap**           |
# | Continuous subarray + sum                | **Prefix Sum** should come to mind |
# | Positive numbers + subarray sum/window   | **Sliding Window** may be better   |
