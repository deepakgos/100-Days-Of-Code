arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# max_local = max_so_far = arr[0]
max_local = max_so_far = float('-inf')

for num in arr:
    max_local = max(num, max_local + num)
    max_so_far = max(max_local, max_so_far)

print(max_so_far)

# Kadane's algorithm