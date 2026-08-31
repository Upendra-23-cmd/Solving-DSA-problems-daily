# Question 6: Intersection of Two Arrays

# Problem Statement
# Given two integer arrays, arr1 and arr2, find all the common elements between them.
# Each common element should appear only once in the output.
# The order of elements in the output does not matter.

# Input Format
# First line: Integer N, size of the first array
# Second line: N space-separated integers
# Third line: Integer M, size of the second array
# Fourth line: M space-separated integers

# Output Format
# Print all the unique elements that are present in both arrays.

# Constraints
# 1 ≤ N, M ≤ 10^5
# -10^9 ≤ arr1[i], arr2[i] ≤ 10^9

# Example Input
# 6
# 1 2 2 3 4 5
# 5
# 2 2 3 6 7
# Example Output
# 2 3

# Your analysis
# Answer exactly in this format:
# Input:
# Goal:
# Important clue:
# Brute force:
# Brute force complexity:
# Constraint check:
# Repeated work:
# Pattern / Algorithm:
# Why?

def intersection_of_arrays(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    result = set1 & set2
    return result

arr1 = [1, 2, 2, 3, 4, 5]
arr2 = [2, 2, 3, 6, 7]
print(intersection_of_arrays(arr1, arr2))  # Output: {2, 3}

# NOTE: operator & is used to find the intersection of two sets. It returns a new set containing elements that are present in both sets.
#       operator | is used to find the union of two sets. It returns a new set containing all unique elements from both sets.
#       operator - is used to find the difference between two sets. It returns a new set containing elements that are present in the first set but not in the second set.
#       operator ^ is used to find the symmetric difference between two sets. It returns a new set containing elements that are present in either of the sets but not in both.
#       operator <= is used to check if the first set is a subset of the second set. It returns True if all elements of the first set are present in the second set, otherwise it returns False.
#       operator >= is used to check if the first set is a superset of the second set. It returns True if all elements of the second set are present in the first set, otherwise it returns False.
#       operator == is used to check if two sets are equal. It returns True if both sets contain the same elements, otherwise it returns False.
#       operator != is used to check if two sets are not equal. It returns True if the sets contain different elements, otherwise it returns False.
#       operator in is used to check if an element is present in a set. It returns True if the element is found in the set, otherwise it returns False.
#       operator not in is used to check if an element is not present in a set. It returns True if the element is not found in the set, otherwise it returns False.


def intersection_of_arrays_2(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    result = set()

    for num in set1:
        if num in set2:
            result.add(num)

    return result

print(intersection_of_arrays_2(arr1, arr2))  # Output: {2, 3}