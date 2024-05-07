

def binary_search(start, end, arr, target):
    while start <= end:
        mid = (start + end)//2

        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            end = mid-1
        else:
            start = mid + 1
    return -1


arr = [2, 3, 4, 10, 40 ]

start = 0
end = len(arr)-1
target = 10

result = binary_search(start, end, arr, target)

if result == -1:
    print("Number not present")
else:
    print("Number present")

