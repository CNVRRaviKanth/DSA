def two_sum(arr,target):
    hashmap = dict()
    for i in range(len(arr)):
        complement = target-arr[i]
        if complement in hashmap:
            return [hashmap[complement,i]]
        
        hashmap[arr[i]] = i

    return "pair not found"

arr = [2, 7, 11, 15]
target = 9
ans = two_sum(arr,target)
print(ans)