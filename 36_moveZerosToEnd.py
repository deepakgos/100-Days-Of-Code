def moveZeroesToEnd(arr, n):
    j = -1
    for i in range(n):
        if arr[i] == 0:
            j = i
            break

    for i in range(j+1, n):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

arr = [3,6,1,0,6,0,2,0]
n = len(arr)

moveZeroesToEnd(arr, n)

print(arr)
    