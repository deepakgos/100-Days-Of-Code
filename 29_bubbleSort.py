def bubbleSort(arr,n):
    for i in range(0,n-1):      
        swapped = False
        
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break

arr = [64, 34, 25, 12, 22, 11, 19]
n = len(arr)

bubbleSort(arr, n)

print(arr)