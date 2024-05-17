def isDifference(arr, x):
    set_num = set(arr)
    for num in arr:
        if num - x in set_num:
            return 1
    return 0
arr = [12,33,11,43,72]
x = 21

result = isDifference(arr,x)
if result:
    print("Differnce is present in the array")

else:
    print("Difference is NOT present in the array")