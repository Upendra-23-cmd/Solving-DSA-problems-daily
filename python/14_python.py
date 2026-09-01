# Problem Statement
# Given an array of integers containing both positive and negative numbers, rearrange the array so that all negative numbers appear before all non-negative numbers.
# The relative order of the elements does not need to be preserved.
# Return the rearranged array.

# Input Format
# First line: Integer N
# Second line: N space-separated integers.

# Output Format
# Print the rearranged array with all negative numbers on the left and non-negative numbers on the right.

# Constraints
# 1 ≤ N ≤ 10^5
# -10^9 ≤ arr[i] ≤ 10^9

# Example Input
# 8
# 1 -2 3 -4 5 -6 -7 8

# Example Output
# -7 -2 -6 -4 5 3 1 8

# Note: Other arrangements are also valid, for example:
# -2 -4 -6 -7 1 3 5 8
# because the question only requires negative numbers to be before non-negative numbers.

def rearrange_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        while left <= right and arr[left] <0 :
            left += 1
        while left <= right and arr[right] >= 0:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1


    return arr

arr = [1, -2, 3, -4, 5, -6, -7, 8]
print(rearrange_array(arr))  # Output: [-2, -4, -6, -7, 5, 3, 1, 8] or any other valid arrangement
    

