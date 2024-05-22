def  getMajority(arr,n):
    my_dict = {}

    for num in arr:
        my_dict[num] = my_dict.get(num,0) + 1
    
    maxNum = max(my_dict,key = my_dict.get)
    maxValue = max(my_dict.values())
    print(my_dict)
    print("MaxKey: ",maxNum)
    print("MaxValue: ",maxValue)

    if maxValue > n / 2:
        print("Majority Element:", maxNum)
    else:
        print("No Majority Element")

arr = [1,2,2,2,3,3,5,4,4,4,4,4,4,4,4]
n = len(arr)

getMajority(arr,n)