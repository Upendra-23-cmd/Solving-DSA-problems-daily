# Next Question
# A warehouse has N boxes arranged in a row. Each box has a positive integer weight.
# The warehouse manager wants to divide the boxes into contiguous groups. Every group must contain at least one box.
# The cost of a group is the sum of weights of the boxes in that group.
# The manager can create at most K groups. Find the minimum possible value of the largest group cost.
# Input Format
# First line: two integers N and K
# Second line: N space-separated positive integers representing box weights.
# Output Format
# Print the minimum possible value of the largest group cost.
# Constraints
# 1 ≤ K ≤ N
# 1 ≤ N ≤ 2 × 10⁵
# 1 ≤ arr[i] ≤ 10⁹
# Example Input
# 5 2
# 7 2 5 10 8
# Example Output
# 18
# Example Explanation
# One optimal division is:
# [7, 2, 5] [10, 8]
# The group costs are 14 and 18, so the largest cost is 18.

def minimum_largest_group(arr, k):
    left, right = max(arr), sum(arr)

    while left < right:
        mid = (left + right) // 2
        current_sum = 0
        groups = 1

        for weight in arr:
            if current_sum + weight > mid:
                groups += 1
                current_sum = weight
            else:
                current_sum += weight

        if groups > k:
            left = mid + 1
        else:
            right = mid

    return left

arr = [7, 2, 5, 10, 8]
k = 2
print(minimum_largest_group(arr, k))  # Output: 18

