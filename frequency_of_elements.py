def frequency(arr):
    hashmap = dict()

    for i in range(len(arr)):
        if arr[i] not in hashmap:
            hashmap[arr[i]] = 1
        else:
            hashmap[arr[i]] = hashmap.get(arr[i],0) + 1

arr = [10,4,7,8,10,9,4,7,2]
frequency(arr)