# Question 5: First Repeating Element
# Problem Statement
# Given an array of N integers, find the first element that repeats in the array.
# Return the element whose first occurrence appears earliest among all repeating elements.
# If no element repeats, return -1.

# Input Format
# First line: Integer N
# Second line: N space-separated integers

# Output Format
# Print the first repeating element. If no repeating element exists, print -1.

# Constraints
# 1 ≤ N ≤ 10^5
# -10^9 ≤ arr[i] ≤ 10^9

# Example Input
# 7
# 10 5 3 4 3 5 6
# Example Output
# 5

# Important note about the example
# Both 5 and 3 repeat:
# 5 → first appears at index 1
# 3 → first appears at index 2
# Therefore, the answer is:
# 5
# Now analyze it without looking for an algorithm yet. Answer exactly in this format:

# Input: array of N integers
# Goal: find first element that repeats in the array
# Important clue: first occurrence,first element that repeats 
# Brute force: check each element for it repearition and keeo track which appears first
# Brute force complexity: O(n^2)
# Constraint check: O(nlogn) or O(n) acceptable
# Repeated work: check and store the first occurrence of each element   
# Pattern / Algorithm: Hash map
# Why? : bacause hashmap store value in the form of key value pairs and we can store value as its frequency of appearance in the array and also we can store the index of first occurrence of each element in the array.


def first_repeating_element(arr):
    occurences = {}
    for num in arr:
        if num in occurences:
            occurences[num] += 1
        else:
            occurences[num] = 1
    
    for num in arr:
        if occurences[num] > 1:
            return num
    return -1

arr = [10, 5, 3, 4, 3, 5, 6]
print(first_repeating_element(arr))  # Output: 5
