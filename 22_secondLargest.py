def secondLargest(arr,n):
    largest = float('-inf')
    slargest = float('-inf')

    for num in arr:
        if num > largest:
            slargest = largest
            largest = num
        if num < largest and num > slargest:
            slargest = num
    return slargest
    
arr = [1,33,23,53,90,12,78,63]
n = len(arr)

result = secondLargest(arr,n)

arr.sort()
print(arr)
print("Second Largest element in the array is: ",result)