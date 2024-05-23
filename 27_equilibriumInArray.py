def equilibrium(arr, n):
    leftSum = 0
    totalSum = sum(arr)

    for i, num in enumerate(arr):
        totalSum -= num

        if leftSum == totalSum:
            return i
        leftSum += num
    return -1

arr = [-7,1,5,2,-4,3,0]

n = len(arr)

result = equilibrium(arr, n)

if result != -1:
    print("Equilibrium index is: ", result)
else:
    print("No equilibrium index found.")
