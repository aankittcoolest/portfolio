
## Climb stairs
- Ref:

### Approach
- dynamic-programming

```py
class Solution:
    def climbStairs(self, n: int) -> int:
        def climbRecursive(m, dp):
            if m == 1:
                return 1
            if m == 2:
                return 2

            if dp[m] is None:
                dp[m] = climbRecursive(m-1, dp) + climbRecursive(m-2, dp)
            return dp[m]

        def climbRecursiveBottomUp(m):
            one = 1
            two = 1

            # this array is just used for visualisation
            a = [0] * m
            a[m-1] = one
            a[m-2] = two
            for i in range(len(a)-2, -1, -1):
                temp = one
                one = one + two
                two = temp
                a[i] = one
                print(a)

            # actual code can be solved like this
            for i in range(m-1):
                temp = one
                one = one + two
                two = temp
            
            return one

        return climbRecursiveBottomUp(n)


sol = Solution()
sol.climbStairs(5)
```