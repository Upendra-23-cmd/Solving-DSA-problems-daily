# ARRAYS — Question 4: Best Time to Buy and Sell Stock
# Problem Statement
# You are given an array prices, where prices[i] represents the price of a stock on day i.
# You can buy the stock once and sell it once on a later day.
# Find the maximum profit you can make.
# If no profit is possible, return 0.

# Input Format
# First line: Integer N
# Second line: N space-separated integers representing stock prices.

# Output Format
# Print the maximum possible profit.

# Constraints
# 2 ≤ N ≤ 10^5
# 0 ≤ prices[i] ≤ 10^9

# Example Input
# 6
# 7 1 5 3 6 4
# Example Output
# 5

# Explanation
# Buy at:
# 1
# and sell later at:
# 6
# Profit:
# 6 - 1 = 5

def max_profiit(arr):
    min_price= arr[0]
    max_profit = 0

    for price in arr:
        if price < min_price:
            min_price = price
        profit = price - min_price
        if max_profit < profit:
            max_profit = profit
    return max_profit

arr = [7, 1, 5, 3, 6, 4]
print(max_profiit(arr))  # Output: 5