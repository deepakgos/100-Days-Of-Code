def getPivot(arr):
    n = len(arr)
    pivot = arr[n-1]
    actual_pivot_index = 0

    for j in range(n):
        if arr[j] <= pivot:
            arr[actual_pivot_index],arr[j] = arr[j],arr[actual_pivot_index]
            actual_pivot_index += 1
    arr[actual_pivot_index],arr[n-1] = arr[n-1],arr[actual_pivot_index]
    return actual_pivot_index

arr = [1,3,2,45,36,12,33,6]  
last_element = arr[-1]


result = getPivot(arr)

print(f"Correct position of last element {last_element} is : ",result)
arr.sort()
print(arr)
