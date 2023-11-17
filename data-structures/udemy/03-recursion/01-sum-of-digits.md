

### Sum of digits using recursion
- Calculate the sum of digits of positive number using recursion.

```
Example:
554

Output:
5 + 5 + 4 = 14
```

## Approach
- We try to solve the problem using recursion.

```py
def sum_of_digits(n):
    assert n >= 0 and int(n) == n, ' The number has to be a positive integer number'
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n//10)


print(sum_of_digits(554))
```