# Question: 52
# A delivery company has N packages arranged in a line. Each package has a weight.
# Find the longest continuous group of packages whose total weight does not exceed K.

# Input Format
# First line contains two integers N and K.
# Second line contains N positive integers representing package weights.

# Output Format
# Print the maximum number of consecutive packages satisfying the condition.

# Constraints
# 1 ≤ N ≤ 10⁵
# 1 ≤ K ≤ 10⁹
# 1 ≤ A[i] ≤ 10⁴

# Example Input
# 8 10
# 2 1 5 1 3 2 1 4
# Example Output
# 4

def longest_continuous_packages(arr, k):
    left = 0
    current_sum = 0
    max_length = 0

    for right in range(len(arr)):
        current_sum += arr[right]

        while current_sum > k:
            current_sum -= arr[left]
            left += 1
        max_length = max(max_length, right - left + 1)

    return max_length

arr = [2, 1, 5, 1, 3, 2, 1, 4]
k = 10
print(longest_continuous_packages(arr, k))  # Output: 4