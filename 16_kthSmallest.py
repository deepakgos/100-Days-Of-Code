def kth_largest_smallest(arr, k):
    if k < 1 or k > len(arr):
        return "Invalid value of k"

    def partition(arr, low, high):
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i

    def quick_select(arr, low, high, k):
        if low <= high:
            pivot_index = partition(arr, low, high)
            if pivot_index == k - 1:
                return arr[pivot_index]
            elif pivot_index > k - 1:
                return quick_select(arr, low, pivot_index - 1, k)
            else:
                return quick_select(arr, pivot_index + 1, high, k)

    return quick_select(arr, 0, len(arr) - 1, k)

arr = [7, 10, 4, 3, 20, 15]
k = 3
print(f"{k}th smallest element:", kth_largest_smallest(arr, k))
print(f"{k}th largest element:", kth_largest_smallest(arr, len(arr) - k + 1))



