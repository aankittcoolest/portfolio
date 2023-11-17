
## 2D Lists
Given 2D list calculate the sum of diagonal elements.


```
Example
myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
diagonal_sum(myList2D) # 15
```

## Approach
- Loop through 2D array and take sum of diagnol elements
- TC: O(n)
- SC: O(1)

```py
def diagonal_sum(matrix):
    sum  = 0
    for i, arr in enumerate(matrix):
        sum = sum + arr[i]
        print(i, arr)
    return sum

print(diagonal_sum([[1,2,3],[4,5,6],[7,8,9]]))
```