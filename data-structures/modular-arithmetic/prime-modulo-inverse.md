## Problem Description
Given two integers A and B. Find the value of A-1 mod B where B is a prime number and gcd(A, B) = 1.

A-1 mod B is also known as modular multiplicative inverse of A under modulo B.



## Problem Constraints
```
1 <= A <= 109
1<= B <= 109
B is a prime number
```



## Input Format
```
First argument is an integer A.
Second argument is an integer B.
```



## Output Format
```
Return an integer denoting the modulor inverse
```



## Example Input
Input 1:

```
 A = 3
 B = 5
```
Input 2:

```
 A = 6
 B = 23
```


## Example Output
Output 1:

```
 2
```
Output 2:

```
 4

```

## Approach

```go
// we will use fermat theorem
// A ^ (-1) mod B = A ^ (B-2) % B
func solve(A int, B int) int {
	return powerMod(A, B-2, B)
}

func powerMod(a int, n int, modulo int) int {
	if n == 0 {
		return 1
	}
	y := powerMod(a, n/2, modulo)
	if n%2 == 0 {
		return (y * y % modulo) % modulo
	}
	return (y % modulo * y % modulo * a % modulo) % modulo
}
```