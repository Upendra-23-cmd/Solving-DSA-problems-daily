# Question 1
# A company monitors the number of requests received by its server every minute.
# Given an array A of N integers, find the maximum total number of requests received in any continuous period of exactly K minutes.

# Input Format
# First line: two integers N and K
# Second line: N integers representing requests received each minute.

# Output Format
# Print the maximum total number of requests received during any continuous period of K minutes.

# Constraints
# 1 ≤ K ≤ N ≤ 10^5
# 0 ≤ A[i] ≤ 10^4

# Example Input
# 8 3
# 2 1 5 1 3 2 6 1

# Example Output
# 11

# Your turn.
# Don't ask me what topic this is. Analyze it yourself using:
# Input
# Goal
# Important clue
# Brute force
# Brute force complexity
# Constraint check
# Repeated work
# Pattern / Algorithm
# Why?

def max_request(arr, k):
    max_sum = 0
    current_sum = sum(arr[:k])
    max_sum = current_sum

    for i in range(k, len(arr)):
        current_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, current_sum)

    return max_sum

arr = [2, 1, 5, 1, 3, 2, 6, 1]
print(max_request(arr, 3))  # Output: 11