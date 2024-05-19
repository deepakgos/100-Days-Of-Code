def reverse_arr(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    # print(arr)

def rotateKTimes(arr,n,d):
    d = d%n
    reverse_arr(arr,0,d-1)
    print(arr)
    reverse_arr(arr,d,n-1)
    print(arr)
    reverse_arr(arr,0,n-1)
    print(arr)

arr = [2,3,1,56,22,2,6,8,9]
n = len(arr)
d = 2

# reverse_arr(arr,d,n-1)
rotateKTimes(arr,n,d)