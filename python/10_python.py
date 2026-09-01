# Question 1: Move Zeroes to the End
# Problem Statement
# Given an array of integers, move all 0s to the end of the array while maintaining the relative order of all non-zero elements.
# You must modify the array rather than creating a completely separate array for the result.

# Input Format
# First line: Integer N
# Second line: N space-separated integers

# Output Format
# Print the modified array.

# Constraints
# 1 ≤ N ≤ 10^5
# -10^9 ≤ arr[i] ≤ 10^9

# Example Input
# 7
# 0 1 0 3 12 0 5
# Example Output
# 1 3 12 5 0 0 0
# Notice:
# Original non-zero elements:
# 1 3 12 5

# Their order stays the same.

# All zeroes move to the end.
# Now don't solve it yet.
# Answer exactly:
# 1. Input:
# 2. Goal:
# 3. Important clue:
# 4. Brute force:
# 5. Brute force complexity:
# 6. Constraint check:
# 7. Repeated work:
# 8. Pattern / Algorithm:
# 9. Why?

def move_zeroes_to_end(arr):
    n = len(arr)
    non_zero_index = 0

    for i in range(n):
        if arr[i] != 0:
            arr[non_zero_index] = arr[i]
            non_zero_index += 1
    
    for i in range(non_zero_index, n):
        arr[i]= 0

    return arr

arr = [0, 1, 0, 3, 12, 0, 5]
print(move_zeroes_to_end(arr))  # Output: [1, 3, 12, 5, 0, 0, 0]