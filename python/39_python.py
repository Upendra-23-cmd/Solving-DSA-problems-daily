# Problem Statement
# You are given an array of N integers representing the prices of a stock over N consecutive days.
# For each day, determine how many consecutive days including the current day the stock price has been less than or equal to the current day's price, looking backward.
# In other words, starting from the current day, move left until you find a day whose price is greater than the current price.

# Input Format
# First line: integer N
# Second line: N space-separated integers.

# Output Format
# Print N integers representing the span for each day.

# Constraints
# 1 ≤ N ≤ 10^5
# 1 ≤ arr[i] ≤ 10^9

# Example
# Input
# 7
# 100 80 60 70 60 75 85
# Output
# 1 1 1 2 1 4 6

# Another Example
# Input
# 5
# 10 20 30 40 50
# Output
# 1 2 3 4 5

def stock_span(arr):
    n = len(arr)
    result = [0] * n
    stack = []

    for i in range(n):
        count = 1
        while stack and stack[-1][0] <= arr[i]:
            count += stack.pop()[1]

        result[i] = count
        stack.append((arr[i], count))

    return result

arr = [100, 80, 60, 70, 60, 75, 85]
print(stock_span(arr))  # Output: [1, 1, 1, 2, 1, 4, 6]