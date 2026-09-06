# Next Question
# A company has N employees standing in a line. Each employee has a performance score.
# For a team-building exercise, the company wants to choose some employees such that no two chosen employees are standing next to each other.
# The total team score is the sum of the selected employees' scores.
# Find the maximum possible team score.

# Input Format
# The first line contains an integer N.
# The second line contains N space-separated integers representing employee scores.

# Output Format
# Print the maximum possible team score.

# Constraints
# 1 ≤ N ≤ 2 × 10⁵
# 1 ≤ arr[i] ≤ 10⁹

# Example Input
# 6
# 5 1 2 10 6 2
# Example Output
# 17
# Example Explanation
# One optimal selection is:
# 5 + 2 + 6 + 2 = 15
# But another valid selection is:
# 5 + 10 + 2 = 17
# No two selected employees are adjacent.
