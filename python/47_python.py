# Problem
# Given an array of integers, find the smallest positive integer that does not appear in the array.

# Input Format
# N
# arr[0] arr[1] ... arr[N-1]

# Output Format
# Print the smallest positive integer missing from the array.

# Constraints
# 1 ≤ N ≤ 10^5
# -10^9 ≤ arr[i] ≤ 10^9

# Example 1
# 5
# 3 4 -1 1 2
# Output:
# 5
# Example 2
# 5
# 1 2 0 -1 -2
# Output:
# 3
# Example 3
# 4
# 7 8 9 11
# Output:
# 1

def missing_interger(arr):
    seen = set()
    for num in arr:
        if num >0 :
            seen.add(num)
    ans = 1
    while ans in seen:
        ans += 1

    return ans

arr = [3, 4, -1, 1, 2]
print(missing_interger(arr))  # Output: 5