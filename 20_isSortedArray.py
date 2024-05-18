def isSorted(arr):
    for i in range(1,len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return True

# arr = [1,2,2,3,4,7,7,9]

# arr = [-1,1,4,8,5,2]

arr = [-2,-5,3,0,1,7]

result = isSorted(arr)

if result:
    print("Array is sorted. Ascending")
    print(arr)
else:
    print("Array is not sorted")
    print(arr)
