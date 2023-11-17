
def diagonal_sum(matrix):
    sum  = 0
    for i, arr in enumerate(matrix):
        sum = sum + arr[i]
        print(i, arr)
    return sum

print(diagonal_sum([[1,2,3],[4,5,6],[7,8,9]]))
