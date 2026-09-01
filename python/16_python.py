# ARRAYS — Question 7: Rotate an Array
# Given an array of N integers, rotate the array to the right by K positions.
# Input Format
# N
# array elements
# K

# Output Format
# Print the rotated array.

# Constraints
# 1 ≤ N ≤ 10^5
# 0 ≤ K ≤ 10^9
# -10^9 ≤ arr[i] ≤ 10^9

# Example Input
# 7
# 1 2 3 4 5 6 7
# 3

# Example Output
# 5 6 7 1 2 3 4

# Understand the example
# Original:
# 1 2 3 4 5 6 7
# Rotate right once:
# 7 1 2 3 4 5 6
# Rotate right twice:
# 6 7 1 2 3 4 5
# Rotate right three times:
# 5 6 7 1 2 3 4

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    
def rotate_array(arr, k):
    n = len(arr)
    k = k % n

    reverse(arr, 0, n - 1)
    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)

    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(rotate_array(arr, k))  # Output: [5, 6, 7, 1, 2, 3, 4]