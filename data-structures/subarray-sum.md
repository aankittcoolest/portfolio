---
lang: en-US
title: Sub-matrix sum
description: Sub matrix sum
---

# Sum of a sub-matrix
## Question

**Given a matrix of size N x M and Q queries, for each query find sum of given submatrix.**

**NOTE**: TL is top-left and BR is bottom-right

### Brute force approach

**IDEA**: For every query we need to iterater from TL to BR and get the sum.

::: tip Complexity
Time Complexity: O(Q \* N \*M) <br>
Space Complexity: O(1)
:::


### Prefix sum approach

1. For one dimensional array psum[i] = sum of all elements from 0 to i
```sh
psum[i] = A[0] + A[1] + ... + A[i]
```

2. For two dimensional array psum[i][j] = sum of all elements from [0][0] to [i][j]
```sh
psum[i][j] = A[0][0] + A[0][1] + ... + A[0][j]
             + A[1][0] + A[1][1] + ... + A[1][j] 
             + A[i][0] + A[i][1] + ... + A[i][j]
```


```go
package main
import "fmt"

func main() {
    fmt.Println("hello ankit")
}
```