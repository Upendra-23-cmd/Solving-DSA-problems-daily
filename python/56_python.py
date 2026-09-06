# Next question — different topic
# A security system generates a sequence of N integer codes. Two codes are considered a valid pair if:
# they occur at different positions, and
# their sum is exactly X.

# The system needs to know how many such pairs of positions exist.
# If the same value appears multiple times, each different pair of positions must be counted separately.

# Input Format
# First line: two integers N and X
# Second line: N space-separated integers

# Output Format
# Print the number of valid pairs.

# Constraints
# 1 ≤ N ≤ 2 × 10⁵
# -10⁹ ≤ arr[i], X ≤ 10⁹

# Example Input
# 6 10
# 2 8 3 7 2 5
# Example Output
# 3

def count_valid_pairs(arr, x):
    count = 0
    freq = {}

    for num in arr:
        complement = x-num
        if complement in freq:
            count += freq[complement]

        freq[num] = freq.get(num, 0) + 1

    return count

arr = [2, 8, 3, 7, 2, 5]
x = 10
print(count_valid_pairs(arr, x))  # Output: 3
