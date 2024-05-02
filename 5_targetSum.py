# Given a list of numbers, return indices of the two numbers such that they add up to a sepcific target.

def targetSum(target, arr):
    num_dict = {}

    for index, number in enumerate(arr):
        complement = target - number
        if complement in num_dict:
            return [num_dict[complement], index]
        
        num_dict[number] = index

    return []

nums = [2, 5, 7, 8, 9]
target = 10

print(targetSum(target, nums))


# The issue in your code lies in the iteration over the arr. 
# When you iterate over arr, you should unpack each element as a tuple (index, number),
# but it seems you're attempting to unpack them directly as if arr contained tuples.
# However, arr is a list of numbers, not a list of tuples.

# To fix this, you can use enumerate() to iterate over arr, which returns both the index and the value at each iteration.