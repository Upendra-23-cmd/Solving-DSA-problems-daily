# Problem Statement
# Given an array of integers, find the length of the longest contiguous subarray that contains only positive numbers.
# A subarray must contain consecutive elements from the original array.

# Input Format
# First line: an integer N
# Second line: N space-separated integers representing the array.

# Output Format
# Print a single integer representing the length of the longest contiguous subarray containing only positive numbers.

# Constraints
# 1 ≤ N ≤ 10^5
# -10^9 ≤ arr[i] ≤ 10^9

# Example Input
# 10
# 1 2 0 4 5 6 -2 3 4 5
# Example Output
# 3

# Your analysis
# Answer exactly:
# 1. Input:
# 2. Goal:
# 3. Important clue:
# 4. Brute force:
# 5. Brute force complexity:
# 6. Constraint check:
# 7. Repeated work:
# 8. Pattern / Algorithm:
# 9. Why?

def longest_positive_subarray(arr):
    max_lenth  = 0
    current_length = 0

    for num in arr:
        if num >0:
            current_length += 1
            max_length = max(max_lenth, current_length)
        else:
            current_length = 0
    return max_length

arr = [1, 2, 0, 4, 5, 6, -2, 3, 4, 5]
print(longest_positive_subarray(arr))  # Output: 3