## approach: first find the frequencies of all elements then loop through the array and find which element comes first with the frequency 1.

def first_unique_number(arr):
    hashmap = dict()

    for i in range(len(arr)):
        if arr[i] in hashmap:
            hashmap[arr[i]] = hashmap.get(arr[i],0) + 1

        hashmap[arr[i]] = 1

    for i in range(len(arr)):
        if hashmap[arr[i]] == 1:
            return arr[i]

arr = [4, 5, 1, 2, 0, 4]
first_unique_number(arr)