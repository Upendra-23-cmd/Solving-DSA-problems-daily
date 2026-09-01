# Question 9: Find the Missing Number
# Problem Statement
# You are given an array containing N distinct integers taken from the range 0 to N.
# Exactly one number is missing from this range.
# Find and return the missing number.

# Input Format
# First line: Integer N
# Second line: N space-separated integers

# Output Format
# Print the missing number.

# Constraints
# 1 ≤ N ≤ 10^5
# All elements are distinct.
# 0 ≤ arr[i] ≤ N

# Example Input
# 5
# 3 0 1 4 5
# Example Output
# 2

# Explanation:
# The complete range should be:
# 0 1 2 3 4 5
# 2 is missing.

# Now analyze it before thinking about the solution.

# Answer exactly:
# Input:
# Goal:
# Important clue:
# Brute force:
# Brute force complexity:
# Constraint check:
# Repeated work:
# Pattern / Algorithm:
# Why?

def find_missing_number(arr,n):
    expected_sum = n*(n + 1) // 2
    actual_sum = 0
    for num in arr:
        actual_sum += num
    return expected_sum - actual_sum

arr = [3, 0, 1, 4, 5]
n = 5
print(find_missing_number(arr, n))  # Output: 2