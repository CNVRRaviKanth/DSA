def single_number(arr):
    hashmap = dict()

    for i in range(len(arr)):
        if arr[i] not in hashmap:
            hashmap[arr[i]] = 1

        else:
            hashmap[arr[i]] = hashmap.get(arr[i],0) + 1

    for k,v in hashmap.items():
        if v == 1:
            return k
        

arr = [4,1,2,1,2]
ans = single_number(arr)
print(ans)