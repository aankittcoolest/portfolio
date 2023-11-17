

## productofArray
Write a function called productOfArray which takes in an array of numbers and returns the product of them all.

```
Examples

productOfArray([1,2,3]) #6
productOfArray([1,2,3,10]) #60
```

### Approach

```py
def productOfArray(arr):
    assert len(arr) > 0 , "Length of array should be greater than zero."
    if len(arr) == 1:
        return arr[0]
    return arr[0] * productOfArray(arr[1:])


print(productOfArray([1,2,3,4]))
print(productOfArray([]))
```