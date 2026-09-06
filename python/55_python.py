# Problem
# A logistics company tracks the number of packages processed by a sorting machine each hour. The machine records N hourly values.
# The manager wants to select exactly K consecutive hours for a performance report. Among all possible selections, the report should use the group whose average processing count is the highest.
# Find the maximum possible average.
# Input Format
# The first line contains two integers N and K.
# The second line contains N space-separated integers representing the packages processed each hour.
# Output Format
# Print the maximum average that can be obtained by selecting exactly K consecutive hours.
# Print the answer rounded to 2 decimal places.
# Constraints
# 1 ≤ K ≤ N
# K ≤ N ≤ 2 × 10⁵
# 0 ≤ arr[i] ≤ 10⁶
# Example Input
# 6 3
# 4 7 2 9 5 8
# Example Output
# 7.33
# Another Example
# 5 2
# 10 3 8 6 7
# Example Output
# 8.50

def max_average(arr, k):
    current_sum = sum(arr[:k])
    max_sum = current_sum

    for i in range(k, len(arr)):
        current_sum += arr[i] -arr[i-k]
        max_sum = max(max_sum, current_sum)
        max_average = max_sum / k

    return round(max_average, 2)

arr = [4, 7, 2, 9, 5, 8]
k = 3
print(max_average(arr, k))  # Output: 7.33