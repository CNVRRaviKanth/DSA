## maximum subarray sum using kadane's algorithm
## maxEnding which calculates which calculates the maximum subarray sum ending at current element. 

## if the maximum subarray sum at the previous index is positive then we extend the subarray.

## if the maximum subarray sum at the previous index is negative we start a new subarray from the current index.

def kadanes_algorithm(arr):
    maxEnding = arr[0]
    res = arr[0]
    
    for i in range(1,len(arr)):
        
        maxEnding = max(maxEnding+arr[i],arr[i])  

        ## if it is a positive no. then maxEnding, if it is a negative no, then we will simply keep the previous result only.
        
        ## updating the new maximum subarray sum.
        res = max(maxEnding,res)

    return res

arr = [2, 3, -8, 7, -1, 2, 3]
kadanes_algorithm(arr)