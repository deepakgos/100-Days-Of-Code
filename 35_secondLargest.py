def secondLargest(arr, n):
    if n > 1:
        largest = arr[0]
        sLargest = float('-inf')

        for i in range(1, n):
            if arr[i] > largest:
                sLargest = largest
                largest = arr[i]
            if arr[i] != largest and arr[i] > sLargest:
                sLargest = arr[i]
        print("Second Larget: ",sLargest)

arr = [1,4,3,7,3,5,9,8,7,9]
n = len(arr)

secondLargest(arr,n)
