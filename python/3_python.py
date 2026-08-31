# Problem Statement
# Given an array of N integers, find the element that occurs the maximum number of times.
# If more than one element has the same maximum frequency, return the element that appears first in the array.

# Input Format
# First line: An integer N
# Second line: N space-separated integers

# Output Format
# Print the most frequent element.

# Constraints
# 1 ≤ N ≤ 10^5
# -10^9 ≤ arr[i] ≤ 10^9

# Example Input
# 8
# 1 3 2 3 4 3 2 2
# Example Output
# 3

def most_frequent_element(arr):
    frequecy ={}

    for num in arr:
      frequecy[num] = frequecy.get(num, 0) + 1
    max_freq = max(frequecy.values())

    for num in arr:
        if frequecy[num] == max_freq:
            return num
    
arr  = [1, 3, 2, 3, -4, 3, 2, 2, -4, -4 , -4]
print(most_frequent_element(arr))  # Output: 3