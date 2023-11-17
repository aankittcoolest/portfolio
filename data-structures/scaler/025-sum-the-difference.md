

## Calculate sum of the difference
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/100260/assignment/problems/453

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/025-sum-the-difference-question.png)

### Approach

```py
class Solution:
    def solve(self, A):
        A.sort()
        maxSum = 0
        minSum = 0
        mod = 1000000007
        mod = 1e9 + 7
        print(mod)
        for i, element in enumerate(A):
            maxSum = (maxSum + self.power(2, i, mod) * element) % mod
            minSum = (minSum + self.power(2, len(A)-i-1, mod) * element) % mod
        return int((maxSum - minSum + mod) % mod)

    def power(self, n, pow, mod):
        if pow == 0:
            return 1

        p = self.power(n, pow//2, mod)
        res = (p * p) % mod

        if pow % 2 == 0:
            return res
        return (res * n) % mod


sol = Solution()
# print(sol.power(2, 4, 1e9 + 7))
# print(sol.power(2, 5, 1e9 + 7))
print(sol.solve([3, 10, 5]))
```