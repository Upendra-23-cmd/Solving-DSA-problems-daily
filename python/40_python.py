# Problem Statement
# You are given an array of N integers.
# For each element, find the nearest element to its left that is greater than it.
# If no such element exists, print -1.
# The answer for each position should be the value of that nearest greater element.
# Input Format
# First line: integer N
# Second line: N space-separated integers.
# Output Format
# Print N integers.
# Constraints
# 1 ≤ N ≤ 10^5
# -10^9 ≤ arr[i] ≤ 10^9
# Example 1
# Input
# 5
# 10 5 8 3 12
# Output
# -1 10 10 8 -1
# Example 2
# Input
# 6
# 4 7 5 6 2 8
# Output
# -1 -1 7 7 6 -1
# Example 3
# Input
# 5
# 5 4 3 2 1
# Output
# -1 5 4 3 2