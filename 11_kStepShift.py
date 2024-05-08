def shiftKStepRight(arr, k):
    while k:
        last = arr[-1]
        i = len(arr)-1
        while (i>=0):
            if i == 0:
                arr[i] = last
            else:
                arr[i] = arr[i-1]
            i -= 1
        k -= 1
    for j in arr:
        print(j ,end=" ")



arr = [1, 2, 3, 4, 5, 6, 7]

k = 3

shiftKStepRight(arr, k)