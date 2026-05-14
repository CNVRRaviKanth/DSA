## The logic for prefix_sum is  prefixSum[i] = prefixSum[i - 1] + arr[i]. prefixSum is another array which is of the same size as input array. The initial value of prefixSum will contain the first value of arr i.e prefixSum[0] = arr[0]

def prefix_sum(arr):
    n = len(arr)
    prefixSum = [0]*n
    prefixSum[0] = arr[0]

    for i in range(1,n):
        prefixSum[i] = prefixSum[i-1] + arr[i]

    return prefixSum

## The prefixSum array will look something like this [30, 40, 50, 55, 105]

arr = [30, 10, 10, 5, 50]
ans = prefix_sum(arr)
print(ans)
