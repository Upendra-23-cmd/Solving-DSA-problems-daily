# You are given an array of N integers representing temperatures recorded over consecutive days.
# For each day, determine the number of days you must wait until a strictly warmer temperature occurs.
# If there is no future day with a warmer temperature, print 0.

# Input Format
# First line: integer N
# Second line: N space-separated integers.

# Output Format
# Print N integers representing the waiting time for each day.

# Constraints
# 1 ≤ N ≤ 10^5
# -10^9 ≤ arr[i] ≤ 10^9

# Example 1
# Input
# 8
# 73 74 75 71 69 72 76 73
# Output
# 1 1 4 2 1 1 0 0

# Example 2
# Input
# 5
# 30 40 50 60 70
# Output
# 1 1 1 1 0

# Example 3
# Input
# 5
# 70 60 50 40 30
# Output
# 0 0 0 0 0

def warmer_temp(arr):
    n = len(arr)
    result = [0] * n
    stack = []

    for i in  range(n):
        count = 0
        while stack and arr[stack[-1]] < arr[i]:
            index = stack.pop()
            result[index] = i - index

        stack.append(i)
        
    return result

arr = [73, 74, 75, 71, 69, 72, 76, 73]
print(warmer_temp(arr))  # Output: [1, 1, 4, 2, 1, 1, 0, 0]
