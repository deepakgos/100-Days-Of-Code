def waveFormation(arr, n):
    arr.sort()
    for i in range(1,n,2):
        arr[i], arr[i-1] = arr[i-1], arr[i]

arr = [4,1,3,2,6,8,7]

n = len(arr)

waveFormation(arr, n)

print(arr)