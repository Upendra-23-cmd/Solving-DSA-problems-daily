# Question 7: Longest Consecutive Sequence
# Problem Statement
# Given an unsorted array of integers, find the length of the longest sequence of consecutive integers.
# The consecutive numbers do not need to appear next to each other in the array.

# Input Format
# First line: Integer N
# Second line: N space-separated integers

# Output Format
# Print the length of the longest consecutive sequence.

# Constraints
# 1 ≤ N ≤ 10^5
# -10^9 ≤ arr[i] ≤ 10^9

# Example Input
# 6
# 100 4 200 1 3 2

# Example Output
# 4

# Because the longest consecutive sequence is:
# 1, 2, 3, 4

def longest_consecutive_sequence(arr):
    num_set = set(arr)
    longest_streak = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            longest_streak = max(longest_streak, current_streak)
    return longest_streak

arr = [100, 4, 200, 1, 3, 2]
print(longest_consecutive_sequence(arr))  # Output: 4