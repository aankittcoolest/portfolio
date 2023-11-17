

## Power of number
- Calculate the power of number using recursion.

### Approach

```py
def pow(x,n):
    assert int(n) == n, "Exponent must be integer"
    if n == 0:
        return 1
    elif n < 0:
        return 1/x * pow(x,n+1)
    return x * pow(x,n-1)

# print(pow(2,5))
# print(pow(-2,5))
print(pow(2,-1))
```