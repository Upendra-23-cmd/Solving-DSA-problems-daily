# Problem Statement
# Given a sorted array of integers, remove the duplicate elements in-place so that each distinct element appears only once.
# Return the number of unique elements k.
# The first k positions of the array should contain the unique elements in their original sorted order.

# You do not need to worry about the elements after the first k positions.
# Input Format
# First line: Integer N
# Second line: N space-separated integers

# Output Format
# Print:
# The number of unique elements k
# The first k unique elements

# Constraints
# 1 ≤ N ≤ 10^5
# -10^9 ≤ arr[i] ≤ 10^9

# The array is sorted in non-decreasing order.
# Example Input
# 8
# 1 1 2 2 2 3 4 4
# Example Output
# 4
# 1 2 3 4
# Important

def remove_duplicates(arr):
    if len(arr) == 0:
        return 0

    k = 0

    for i in range(1, len(arr)):
        if arr[i] != arr[k]:
            k += 1
            arr[k] = arr[i]
    return k + 1

arr = [1, 1, 2, 2, 2, 3, 4, 4]
k = remove_duplicates(arr)
print(k)  # Output: 4