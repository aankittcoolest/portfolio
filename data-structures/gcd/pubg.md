## Problem Description
There are N players, each with strength A[i]. when player i attack player j, player j strength reduces to max(0, A[j]-A[i]). When a player's strength reaches zero, it loses the game, and the game continues in the same manner among other players until only 1 survivor remains.

Can you tell the minimum health last surviving person can have?



## Problem Constraints
```
1 <= N <= 100000
1 <= A[i] <= 1000000
```

## Examples
Input: 
```
A = [6, 4]
```

Output: 
```
2
```

Input: 
```
A = [2, 3, 4]
```

Output: 
```
1
```

## Approach

```go
func solve(A []int) int {
	ans := A[0]
	for i := 1; i < len(A); i++ {
		ans = gcd(ans, A[i])
	}
	return ans
}

func gcd(A int, B int) int {
	if B == 0 {
		return A
	}
	return gcd(B, A%B)

}kkkkk
```