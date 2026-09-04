# Problem Statement
# You are given an array of N integers.
# For each element, determine the number of consecutive elements immediately to its left that are smaller than or equal to it, stopping as soon as you encounter an element greater than it.
# Return this count for every element.

# Input Format
# First line: integer N
# Second line: N space-separated integers.

# Output Format
# Print N integers representing the count for each position.

# Constraints
# 1 ≤ N ≤ 10^5
# -10^9 ≤ arr[i] ≤ 10^9

# Example 1
# Input
# 7
# 100 80 60 70 60 75 85
# Output
# 1 1 1 2 1 4 6

# Example 2
# Input
# 5
# 10 20 30 40 50
# Output
# 1 2 3 4 5

# Example 3
# Input
# 5
# 50 40 30 20 10
# Output
# 1 1 1 1 1


def count_smaller_elements_left(arr):

    n = len(arr)
    result = [0] * n
    stack = []

    for i in range(n):
        count =1
        while stack and stack[-1][0] <= arr[i]:
            count += stack.pop()[1]
    
        result[i] = count
        stack.append((arr[i], count))

    return result

arr = [100, 80, 60, 70, 60, 75, 85]
print(count_smaller_elements_left(arr))  # Output: [1, 1, 1, 2, 1, 4, 6]


