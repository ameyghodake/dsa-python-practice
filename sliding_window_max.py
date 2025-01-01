# max min subarray substrings

# To find the maximum sum of all subarrays of size K

# Brute Force

import sys

INT_MIN = -sys.maxsize -1

# n length of arra
# k size of window
def maxSum(arr, n, k):
    max_sum = INT_MIN

    for i in range(n - k + 1):
        current_sum = 0
        for j in range(k):
            current_sum = current_sum + arr[i+j]

        max_sum = max(current_sum, max_sum)
    
    return max_sum

arr = [1, 4, 2, 10, 2,
       3, 1, 0, 20]
k = 4
n = len(arr)
print(maxSum(arr, n, k))

# here 2 nested loops hence time complexity -> O(k*n)

## SLIDING WINDOW TECHNIQUE


def max_sum(arr, k):
    n = len(arr)
    if n<=k:
        print("Invalid")
        return -1
    
    # compute sum of first window
    window_sum = sum(arr[:k])

    # first sum available
    max_sum = window_sum
    
    # remaining sums
    # remove first element and adding last element of current window
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(window_sum, max_sum)
    
    return max_sum

print(max_sum(arr, k))