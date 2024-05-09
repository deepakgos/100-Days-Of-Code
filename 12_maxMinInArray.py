def max_min(arr):
    max = min = arr[0]
    for num in arr:
        if num > max:
            max = num
        if num < min:
            min = num
    return (max,min)

arr = [1,4,3,2,6,9,8,5,7]

maxNum, minNum = max_min(arr)

print("Max is: ",maxNum," & Min is: ",minNum)