# ARRAYS — Question 6: Find the Majority Element
# Problem Statement
# Given an array of N integers, find the element that appears more than N/2 times.
# You can assume that a majority element always exists.

# Input Format
# First line: Integer N
# Second line: N space-separated integers.

# Output Format
# Print the majority element.

# Constraints
# 1 ≤ N ≤ 10^5
# -10^9 ≤ arr[i] ≤ 10^9

# Example Input
# 7
# 2 2 1 1 1 2 2
# Example Output
# 2

# Explanation
# There are 7 elements.
# N/2 = 3.5

# The number 2 appears 4 times:
# 2 2 1 1 1 2 2
# ↑ ↑       ↑ ↑
#     4 times
# Since 4 > 3.5, 2 is the majority element.

def majority_element(arr):
    count = {}
    n = len(arr)

    for num in arr:
        count[num] =  count.get(num, 0)+1

    for num in count:
        if count[num] > n // 2:
            return num
        
arr = [2, 2, 1, 1, 1, 2, 2]
print(majority_element(arr))  # Output: 2