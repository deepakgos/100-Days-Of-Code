def merge(arr,left,mid,right):
    subarr1 = mid - left+1
    subarr2= right - mid

    leftsubarr = [0] * subarr1
    rightsubarr = [0] * subarr2

    for i in range(subarr1):
         leftsubarr[i] = arr[left+i]
    for j in range(subarr2):
        rightsubarr[j] = arr[mid+1+j]  

    indexofleftsubarr = 0
    indexofrightsubarr = 0
    indexofmergearr = left

    while indexofleftsubarr < subarr1 and indexofrightsubarr < subarr2:
        if leftsubarr[indexofleftsubarr] <= rightsubarr[indexofrightsubarr]:
            arr[indexofmergearr] = leftsubarr[indexofleftsubarr]
            indexofleftsubarr += 1
        else:
            arr[indexofmergearr] = rightsubarr[indexofrightsubarr]
            indexofrightsubarr += 1
        indexofmergearr += 1

    while indexofleftsubarr < subarr1:
        arr[indexofmergearr] = leftsubarr[indexofleftsubarr]
        indexofleftsubarr += 1
        indexofmergearr += 1

    while indexofrightsubarr < subarr2:
        arr[indexofmergearr] = rightsubarr[indexofrightsubarr]
        indexofrightsubarr += 1
        indexofmergearr += 1

def mergeSort(arr,begin,end):
    if begin >= end:
        return
    
    mid = begin + (end - begin)//2
    mergeSort(arr,begin,mid)
    mergeSort(arr,mid+1,end)
    merge(arr,begin,mid,end)

arr = [12,43,55,11,76,28,92,34,62,7]

n = len(arr)

mergeSort(arr,0,n-1)

print(arr)