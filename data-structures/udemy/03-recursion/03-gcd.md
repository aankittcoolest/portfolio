

## GCD
- Calculate GCD of two numbers using recusion.
- Here we solve the problem using Eucledian algorithm.

### Eucledian Algorithm
- GCD(A,0) = A
- GCD(A,B) = GCD(B,A mod B)


## Approach
- We will solve the problem using recursion.

```py
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a % b)

print(gcd(48,18))
print(gcd(18,48))
```