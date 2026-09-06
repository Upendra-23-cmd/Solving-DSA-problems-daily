# A monitoring system records the status of machines as a binary string.
# A 0 means a machine is inactive and a 1 means it is active.

# You may perform the following operation at most once:
# Choose a continuous section of the string and change every 0 in that section to 1.
# Find the maximum number of active machines that can be obtained.

# Input Format
# The first line contains an integer N.
# The second line contains N binary integers.

# Output Format
# Print the maximum possible number of active machines.

# Constraints
# 1 ≤ N ≤ 10⁵
# A[i] is either 0 or 1

# Example Input
# 7
# 1 0 0 1 0 0 1
# Example Output
# 6

def max_active_machines(arr):
    total_ones = sum(arr)
    max_gain = 0
    current_gain = 0

    for num in arr:
        if num == 0:
            current_gain += 1
        else:
            current_gain -= 1
        
        if current_gain < 0:
            current_gain = 0
        
        max_gain = max(max_gain, current_gain)

    return total_ones + max_gain

arr = [1, 0, 0, 1, 0, 0, 1]
print(max_active_machines(arr))  # Output: 6