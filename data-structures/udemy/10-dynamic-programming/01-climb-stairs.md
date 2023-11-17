

## Climb stairs
- Ref: https://leetcode.com/problems/climbing-stairs/


### Approach

```py
class Solution:
    def climbStairs(self, n: int) -> int:
        def climbRecursiveTopDown(m, dp):
            if m == 1:
                return 1
            if m == 2:
                return 2

            if dp[m] is None:
                dp[m] = climbRecursiveTopDown(m-1, dp) + climbRecursiveTopDown(m-2, dp)
            return dp[m]

        
        def climbRecursiveBottomUp(m):
            one = 1
            two = 1
            for i in range(m-1):
                temp = one
                one = one + two
                two = temp
            return one
            


        # return int(climbRecursiveTopDown(n, [None] * (n+1)))
        return climbRecursiveBottomUp(n)


sol = Solution()
# print(sol.climbStairs(2))
# print(sol.climbStairs(3))
print(sol.climbStairs(10))
```
