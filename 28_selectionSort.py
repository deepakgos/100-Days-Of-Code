def selectionSort(arr):

    for i in range(len(arr)-1):
        min_index = i

        for j in range(i+1,len(arr)):
            if arr[min_index] > arr [j]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index],arr[i]

arr = [3,1,6,4,8,5,9]

selectionSort(arr)

print(arr)

    