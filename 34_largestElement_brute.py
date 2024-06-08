def largestElement(arr, n):
    # arr.sort()
    # print(arr[-1])
    largest = arr[0]
    for i in range(1,n):
        if arr[i] > largest:
            largest = arr[i]
    print(largest)
arr = [1,5,3,7,2,7,9,4]
n = len(arr)

largestElement(arr,n)