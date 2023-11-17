---
lang: en-US
title: Prefix sum two dimensional array
description: Prefix sum two dimensional array
---

# Prefix sum of two dimensional array
## Question

**Given a matrix of size N x M create a prefix sum array**

### Approach


<iframe src="/pdfs/17-prime-numbers.pdf" width="100%" height="1000"></iframe>


```go
func calculate_psum(A [][]int) [][]int64 {

    // initialise a prefix sum array
	B := make([][]int64, len(A))
	for i := range B {
		B[i] = make([]int64, len(A[0]))
	}

	for i := range A {
		B[i][0] = int64(A[i][0])
	}

    //handle columns
	for i := 0; i < len(A); i++ {
		for j := 0; j < len(A[i]); j++ {
			if j > 0 {
				B[i][j] = int64(A[i][j]) + B[i][j-1]
			}
		}
	}

    //handle rows
	for i := 0; i < len(A); i++ {
		for j := 0; j < len(A[i]); j++ {
			if i > 0 {
				B[i][j] = int64(B[i][j]) + B[i-1][j]
			}
		}
	}
	return B
}
```