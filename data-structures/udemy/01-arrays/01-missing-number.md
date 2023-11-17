

## Missing Number

### Question
Write a function to find the missing number in a given integer array of 1 to 100.

Example

```text
missing_number([1, 2, 3, 4, 6], 6) # 5
```

### Approach 1
- Loop through the array and return the missing index since array is sorted
- TC: O(N)
- SC: O(1)

```py
def missing_number(arr, n):
    i=1
    for val in arr:
        if i != val:
            return i
        i = i + 1

print(missing_number([1,2,3,4,6],6))
```

### Approach 2
- Calculate total sum of n numbers and subtract it from the sum of array
- TC: O(N)
- SC: O(1)

```py
def missing_number(arr, n):
    # total sum
    total_sum = n * (n+1)//2

    # sum of array
    array_sum = sum(arr)

    # missing number
    return total_sum - array_sum

print(missing_number([1,2,3,4,6],6))
```