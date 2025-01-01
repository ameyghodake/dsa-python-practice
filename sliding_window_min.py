# returns the length of smallest subarray with sum greater than x

# Two pointers method to maintain sliding window
def smallest_sub_with_sum(x, arr):
    n = len(arr)
    start = 0
    current_sum = 0

    min_length = float('inf')

    for end in range(n):
        # this loop is for the window size of the subarray
        current_sum = current_sum + arr[end]

        # check if sum found to be greater than target
        while current_sum >= x:
            min_length = min(min_length, end-start+1)
            current_sum = current_sum - arr[start]
            start = start + 1
    return min_length if min_length != float('inf') else 0

x = 51
arr = [1, 4, 45, 6, 0, 19]
print(smallest_sub_with_sum(x, arr))
