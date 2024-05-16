def isMajority(arr, x):
    n = len(arr)
    last = (n//2 + 1) if n%2 != 0 else n//2

    for i in range(last):
        if arr[i] == x and arr[i+last] == x:
            return 1
    return 0

arr = [2,3,4,5,5,5,5,5,1,5]
x = 4
majority = isMajority(arr, x)

if majority:
    print(f"{x} is majority element.")
else:
    print(f"{x} is not majority element.")

