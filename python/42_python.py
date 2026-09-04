# Problem Statement
# You are given an array of N integers representing buildings arranged from left to right.
# For each building, determine the first building to its right that is taller than it.
# If no taller building exists, print -1.

# Input Format
# First line: integer N
# Second line: N space-separated integers.

# Output Format
# Print N integers representing the height of the first taller building to the right of each building.

# Constraints
# 1 ≤ N ≤ 10^5
# -10^9 ≤ arr[i] ≤ 10^9

# Example 1
# Input
# 6
# 4 5 2 10 8 7
# Output
# 5 10 10 -1 -1 -1

# Example 2
# Input
# 5
# 3 1 4 2 5
# Output
# 4 4 5 5 -1

# Example 3
# Input
# 5
# 5 4 3 2 1
# Output
# -1 -1 -1 -1 -1

def tall_building(arr):
    n = len(arr)
    result = [-1] * n
    stack = []

    for i in range(n-1 , -1, -1):
        while stack and stack[-1] < arr[i]:
            stack.pop()
        result[i] = stack[-1] if  stack else -1
        stack.append(arr[i])
    return result

arr = [4, 5, 2, 10, 8, 7]
print(tall_building(arr))  # Output: [5, 10, 10, -1, -1, -1]

        