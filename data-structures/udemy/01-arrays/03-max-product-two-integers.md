
## Max Product of Two Integers
- Find the maximum product of two integers in an array where all elements are positive.

```
Example

arr = [1, 7, 3, 4, 9, 5] 
max_product(arr) # Output: 63 (9*7)
```


### Aproach 1
- Technique: Sort the array in reverse order and take product of first two elements
- TC: O(nlog(n))
- SC: O(1)

```py
def max_product(arr):
    arr.sort(reverse=True)
    return arr[0]*arr[1]

print(max_product([1, 7, 3, 4, 9, 5]))
```

### Aproach 2
- Technique: Find two maximum positive numbers and return their sum
- TC: O(n)
- SC: O(1)

```py
def max_product(arr):
    num1 = arr[0]
    num2 = arr[0]
    for num in arr:
        if num > num1:
            num2 = num1
            num1 = num
        elif num > num2:
            num2 = num
    return num1 * num2

print(max_product([1, 7, 3, 4, 9, 5]))
```

