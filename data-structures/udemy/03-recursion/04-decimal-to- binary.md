

## Decimal to binary
- Convert decimal number to binary number using recursion.


### Approach
```py
def decimal_to_binary(a):
    assert int(a) == a , "Only integer values are allowed"
    if a == 0:
        return 0
    return a % 2 + 10 * decimal_to_binary(a//2)

    # return "%s%s" % (decimal_to_binary(a//2), a % 2)


print(decimal_to_binary(10))
print(decimal_to_binary(101))
```