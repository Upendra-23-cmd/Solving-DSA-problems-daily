# Problem
# Given a sorted array of integers and an integer K, determine whether there exists a pair of elements whose sum is exactly K.
# Return True if such a pair exists, otherwise return False.

# Input Format
# N
# arr[0] arr[1] ... arr[N-1]
# K

# Output Format
# True
# or
# False

# Constraints
# 1 ≤ N ≤ 10^5
# -10^9 ≤ arr[i] ≤ 10^9
# -10^14 ≤ K ≤ 10^14

# Example 1
# 6
# 1 2 4 7 11 15
# 15
# Output:
# True
# Because:
# 4 + 11 = 15
# Example 2
# 5
# 1 3 5 8 12
# 20
# Output:
# False
# Example 3
# 6
# -5 -2 1 4 7 10
# 5
# Output:
# True
# Because:
# -2 + 7 = 5

def find_pair_with_sum(arr, k):
    seen = set()
    for num in arr:
        if k - num in seen:
            return True
        seen.add(num)

    return False

arr = [1, 3,5 ,8, 12]
k = 20
print(find_pair_with_sum(arr, k))  # Output: True


# but answere was two pointer because sorted array + pair + target sum = two pointer technique
# if unsorted array then we can use hashset to find the pair with sum k

def find_pair_two_pointer(arr, k):
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == k:
            return True
        elif current_sum < k:
            left += 1
        else:
            right -= 1

    return False

print(find_pair_two_pointer(arr, k))  # Output: true