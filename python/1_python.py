# Problem
# You are given an array of N integers. Determine whether the array contains any duplicate element.

# Return:
# YES → if any number appears more than once
# NO  → if every number is unique

# Input
# N
# a1 a2 a3 ... aN

# Constraints
# 1 ≤ N ≤ 10^5
# -10^9 ≤ ai ≤ 10^9

# Example 1
# Input:
# 5
# 1 2 3 2 5

# Output:
# YES
# Example 2
# Input:
# 5
# 1 2 3 4 5

# Output:
# NO

# Your task
# Analyze it:
# 1. Input:
# 2. Goal:
# 3. Important clue:
# 4. Brute force:
# 5. Brute force complexity:
# 6. Constraint check:
# 7. Repeated work:
# 8. Pattern:
# 9. Why?

# this is how you define a function in python
def contains_duplicate(arr):

    # set is a data structure that stores unique elements for hashset
    seen = set()

    # how to iterate array one by one in for loop
    for num in arr:

        # condition to check if the number is already in the set
        if num in seen:
            return "yes"
        # if the number is not in the set, add it to the set
        seen.add(num)

    # if we reach here, it means there are no duplicates
    return "no"

# define an array of integers
arr = [1, 2, 3, 2, 5]

# call the function and print the result
result = contains_duplicate(arr)
print(result)  # Output: YES