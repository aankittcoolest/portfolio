

## Compute ncr
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/127963/assignment/problems/4111/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/039-compute-ncr-question.png)

### Approach
- Dynamic Programming
- ncr = (n-1)c(r-1) + (n-1)cr
- array size: n*r

```py
class Solution:

    def solve(self, A, B, C):
        dp = [[1 for _ in range(B+1)] for _ in range(A+1)]

        for i in range(0, A+1):
            for j in range(0, min(i, B)+1):
                if j == 0 or j == i:
                    dp[i][j] = 1
                else:
                    dp[i][j] = (dp[i-1][j-1] % C + dp[i-1][j] % C) % C

        return dp[A][B]


sol = Solution()
print(sol.solve(5, 2, 13))
print(sol.solve(6, 2, 13))
print(sol.solve(1000000, 1, 999999))
```
