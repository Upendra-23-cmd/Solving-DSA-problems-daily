# Problem Statement
# Given an array of integers, find the smallest positive integer that is missing from the array.
# The array may contain duplicate values, negative numbers, and zero.
# Input Format
# First line: an integer N
# Second line: N space-separated integers.
# Output Format
# Print the smallest positive integer that does not appear in the array.
# Constraints
# 1 ≤ N ≤ 10^5
# -10^9 ≤ arr[i] ≤ 10^9
# Example Input
# 6
# 3 4 -1 1 2 6
# Example Output
# 5
# Now analyze it using:
# 1. Input:
# 2. Goal:
# 3. Important clue:
# 4. Brute force:
# 5. Brute force complexity:
# 6. Constraint check:
# 7. Repeated work:
# 8. Pattern / Algorithm:
# 9. Why?

def smallest_missing_positive(arr):
    seen = set()
    for num in arr:
        if num > 0:
            seen.add(num)
    answere = 1
    while answere in seen:
        answere += 1
    return answere

arr = [3, 4, -1, 1, 2, 6]
print(smallest_missing_positive(arr))  # Output: 5