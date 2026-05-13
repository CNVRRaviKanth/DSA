def contains_duplicates_hashset(arr):
    hashset = set()

    for i in range(len(arr)):
        if arr[i] in hashset:
            return True
        
        hashset.add(arr[i])
        
    return False


arr = [10,4,7,8,10,9,4,7,2]
ans = contains_duplicates_hashset(arr)
print(ans)