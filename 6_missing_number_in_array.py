def missingNumber(arr):
    last = len(arr)
    xorNum = 0
    for i in range(1,last+2):
        xorNum = xorNum ^ i
    
    xorArr = arr[0]
    for j in range(1,last):
        xorArr = xorArr^arr[j]

    missing_number = xorNum ^ xorArr

    return missing_number

arr = [1,2,3,4,6]

print(missingNumber(arr))