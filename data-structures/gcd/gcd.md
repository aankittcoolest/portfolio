---
lang: en-US
title: GCD
description: GCD
---

# Calculate GCD

## Problem Description
Given 2 non-negative integers A and B, find gcd(A, B)

GCD of 2 integers A and B is defined as the greatest integer 'g' such that 'g' is a divisor of both A and B. Both A and B fit in a 32 bit signed integer.


## Problem Constraints
```text
0 <= A, B <= 109
```



## Input Format
```text
First argument is an integer A.
Second argument is an integer B.
```



## Output Format
```text
Return an integer denoting the gcd(A, B).
```



## Example Input
Input 1:

```text
A = 4
B = 6

```

Input 2:
```text
A = 6
B = 7
```


## Example Output
Output 1:

```text
 2
```
Output 2:

```text
 1
```

**Calculate GCD of two numbers**

### Approach


```go
func gcd(A int, B int) int {
	if B == 0 {
		return A
	}
	return gcd(B, A%B)
}
```

```text
TC = O(log max(a,b))
SC = O(1)
```