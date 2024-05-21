def getLeader(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] <= arr[j]:
                break
            #if loop did not break then
        if j == n-1:
            print(arr[i],end=" ")

arr = [16, 17, 4, 3, 5, 2]

getLeader(arr)