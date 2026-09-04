# Problem Statement
# Given an array of N integers, for every element, find the first greater element appearing to its right.
# If no greater element exists, print -1 for that position.

# Input Format
# First line: integer N
# Second line: N space-separated integers.

# Output Format
# Print N integers representing the first greater element to the right of each element.

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
# 1 3 2 4 5
# Output
# 3 4 4 5 -1
# Example 3
# Input
# 5
# 5 4 3 2 1
# Output
# -1 -1 -1 -1 -1

def first_greater_element(arr):
    n = len(arr)
    result = [-1]* n
    stack = []

    for i in range(n-1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
            
        result[i] = stack[-1] if stack else -1
        stack.append(arr[i])

    return result

arr = [4, 5, 2, 10, 8, 7]
print(first_greater_element(arr))  # Output: [5, 10, 10, -1, -1, -1]
        