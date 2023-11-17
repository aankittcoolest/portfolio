
## Ath magical number
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/120894/assignment/problems/5697/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/029-ath-magical-number-question.png)

### Approach
- binary search

```py
class Solution:
    def solve(self, A, B, C):
        def gcd(a, b):
            if a == 0:
                return b
            return gcd(b % a, a)

        def lcm(a, b):
            return (a*b)//gcd(a, b)

        lcm_result = lcm(B, C)

        def getMagicalNum(m):
            return (m//B) + (m//C) - (m//lcm_result)

        lo = 1
        hi = min(B, C) * A
        mid = hi
        ans = 0

        while lo <= hi:
            mid = (lo + hi)//2
            res = getMagicalNum(mid)
            if res >= A:
                ans = mid
                hi = mid-1
            else:
                lo = mid + 1
        return ans % (10**9 + 7)


sol = Solution()
print(sol.solve(4, 2, 3))
print(sol.solve(1, 2, 3))
print(sol.solve(19, 11, 13))
print(sol.solve(11, 12, 13))
```