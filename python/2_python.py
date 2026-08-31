# Problem
# You are given an array of N integers and a target integer K.
# Determine whether there are two different elements in the array whose sum is equal to K.
# Return:
# YES → if a pair exists
# NO  → if no pair exists

# Input
# N
# a1 a2 a3 ... aN
# K

# Constraints
# 2 ≤ N ≤ 10^5
# -10^9 ≤ ai ≤ 10^9

# Example 1
# Input:
# 5
# 2 7 11 15 3
# 10

# Output:
# YES
# Because:
# 7 + 3 = 10

# Example 2
# Input:
# 4
# 1 4 8 12
# 10

# Output:
# NO

# Your task
# Do not code yet. Analyze the question:

# 1. Input: array and a target integer to check for the no. pair
# 2. Goal: find the sum of two no equal to k
# 3. Important clue: sum of two no. ,,, note : Two numbers + target sum + array is NOT sorted
# 4. Brute force: check for the sum one by one 
# 5. Brute force complexity: o(n^2)
# 6. Constraint check: o(n) acceptable
# 7. Repeated work: again check for the sum
# 8. Pattern: hashmap and hashset combine
# 9. Why? : because we need to find the whether the pair where the sum = to k exist or not  

def has_pair_with_sum(arr, k):
    seen = set()

    for num in arr:
        complement= k-num
        if complement in seen:
            return "yes"
        seen.add(num)
    return "no"

arr = [2, 7, 11, 15, 3]
k = 10
print(has_pair_with_sum(arr, k))  # Output: YES
