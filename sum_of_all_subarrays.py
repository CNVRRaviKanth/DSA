def sum_of_all_subarrays(arr):
    result = 0
    for i in range(len(arr)):
        temp = 0
        for j in range(i,len(arr)):
            temp += arr[j]
            result += temp

    return result

arr = [1, 4, 5, 3, 2]
ans = sum_of_all_subarrays(arr)
print(ans)