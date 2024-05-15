def get_intersection(arr1, arr2, temp, n1, n2):
    i = 0
    j = 0
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j += 1
        else:
            temp.append(arr1[i])
            i += 1
            j += 1
    return temp

arr1 = [1,2,4,6,9,20,35,50]
arr2 = [3,4,6,8,30,35,60]
arr3 = [4,5,8,20,35,40]

n1 = len(arr1)
n2 = len(arr2)
n3 = len(arr3)

temp = []
ans = []

temp = get_intersection(arr1, arr2, temp, n1, n2)
temp_size = len(temp)

ans = get_intersection(arr3, temp, ans, n3, temp_size)

print("Common Elements in three given arrays are: ",ans)