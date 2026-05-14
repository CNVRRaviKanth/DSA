## as the array contains positive numbers we can use sliding window approach

def longest_subarray_with_given_sum_k_positive(arr,k):
    total = 0
    max_size = 0
    left = 0
    for i in range(len(arr)):
        total += arr[i]     ## expanding the window
        while total > k:    ## shrinking the window
            total -= arr[left]
            left += 1

        if total == k:
            max_size = max(max_size,i-left+1)

    return max_size

arr = [10, 5, 2, 7, 1, 9]
k = 15
ans = longest_subarray_with_given_sum_k_positive(arr,k)
print(ans)