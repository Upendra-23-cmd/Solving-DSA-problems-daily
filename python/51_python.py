# Question 2
# A warehouse stores the quantities of products in an array. The quantities are already arranged in non-decreasing order.
# Given an integer X, determine whether there are two different products whose quantities differ by exactly X.

# Input Format
# First line: two integers N and X
# Second line: N integers representing the product quantities.

# Output Format
# Print YES if such a pair exists, otherwise print NO.

# Constraints
# 2 ≤ N ≤ 10⁵
# 0 ≤ X ≤ 10⁹
# 0 ≤ A[i] ≤ 10⁹
# The array is sorted in non-decreasing order.

# Example Input
# 7 5
# 1 3 7 8 12 15 20
# Example Output
# YES

def find_pair_difference(arr, x):
    left = 0
    right =1

    while right < len(arr):
        diff = arr[right] - arr[left]
        if diff == x and left != right:
            return "yes"
        elif diff < x:
            right += 1
        else:
            left += 1
            if left == right:
                right += 1

    return "no"

arr = [1, 3, 7, 8, 12, 15, 20]
x = 5
print(find_pair_difference(arr, x))  # Output: YES