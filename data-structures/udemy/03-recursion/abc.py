

def flatten(arr):
    print(type(arr))
    print(arr.extend(arr[arr[0]]))



print(flatten([[1]]))
# flatten([1,2])
# flatten([])

# print(flatten([1, 2, 3, [4, 5]])) # [1, 2, 3, 4, 5]