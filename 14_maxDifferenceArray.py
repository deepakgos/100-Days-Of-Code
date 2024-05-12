def min_difference(arr):
    arr.sort()
    maxDiff = float("-inf")

    for i in range(len(arr)-1):
        currentDiff = arr[i+1] - arr[i]
        if currentDiff > maxDiff:
            maxDiff = currentDiff
    return maxDiff

arr = [-55,32,45,4,12,118,25]

max_diff = min_difference(arr)
print("Max difference in the array is:",max_diff)
