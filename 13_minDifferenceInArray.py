def min_difference(arr):
    min_diff = float("inf")
    arr.sort()
    print(arr)
    for i in range(len(arr)-1):
        currentDiff = arr[i+1] - arr[i]
        if currentDiff < min_diff:
            min_diff =  currentDiff

    return min_diff

arr = [-55,32,45,4,12,118,25]

min_diff = min_difference(arr)

print("The minimum differnce in the array is :",min_diff)