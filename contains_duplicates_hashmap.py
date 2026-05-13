def contains_duplicate_hashmap(arr):
    hashmap = dict()

    for i in range(len(arr)):
        if arr[i] in hashmap:
            return True
        
        hashmap[arr[i]] = 1

    return False

arr = [10,4,7,8,10,9,4,7,2]
ans = contains_duplicate_hashmap(arr)