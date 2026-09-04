# Given an array of N integers, find the first smaller element on the right for every element.
# For each element, find the first element appearing to its right that is strictly smaller than it.
# If no such element exists, print -1.

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
# 6
# 4 8 5 2 25 7
# Output
# 2 5 2 -1 7 -1
# Example 2
# Input
# 5
# 5 4 3 2 1
# Output
# 4 3 2 1 -1
# Example 3
# Input
# 5
# 1 2 3 4 5
# Output
# -1 -1 -1 -1 -1

def smaller_element_right(arr):
    n = len(arr)
    result = [-1] * n
    stack = []

    for i in range(n-1, -1, -1):
        while stack and stack[-1] >= arr[i]:
            stack.pop()

        result[i] = stack[-1] if stack else -1
        stack.append(arr[i])
    return result

arr = [4, 8, 5, 2, 25, 7]
print(smaller_element_right(arr))  # Output: [2, 5, 2, -1, 7, -1]