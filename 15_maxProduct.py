def max_product(arr):
    maxProd = float("-inf")

    arr.sort()
    for i in range(len(arr)-1):
        currentMaxProd = arr[i] *  arr[i+1]
        if currentMaxProd > maxProd:
            maxProd = currentMaxProd
    return maxProd

arr = [-55,32,45,4,12,118,25]

maximumProd = max_product(arr)

print("Max product in the array is: ",maximumProd)