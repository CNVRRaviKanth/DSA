## sliding window will not work as the array can have both positive and negative numbers so, we can't use expand and shrink concept.

## so, to solve this we are going to use prefix_sum + hashmap approach
## we use prefix_sum to avoid recomputing sums again and again it reuse previously computed sums.

## prefix_sum = sum of elements from 0 to index, i

## eg: arr = [2, 4, 1, 3] prefix_sum -> [2, 6, 7, 10] initially prefix_sum will be 0

## subarray_sum = current_prefix_sum - previous_prefix_sum

## for this problem if we use only prefix_sum we can't determine which subarray is giving the sum which equals k therefore we make use of hashmap.

## current_sum - previous_sum = k -> previous_sum = current_sum - k

def subarray_sum_equals_k(arr,k):
    hashmap = {0:1}
    result = 0
    prefixSum = 0

    for i in range(len(arr)):
        prefixSum+=arr[i]

        if (prefixSum-k) in hashmap:
            result += hashmap.get((prefixSum-k),0)

        hashmap[prefixSum] = hashmap.get(prefixSum,0)+1

    return result


arr = [2, -1, 2]
k = 3
ans = subarray_sum_equals_k(arr,k)
print(ans)