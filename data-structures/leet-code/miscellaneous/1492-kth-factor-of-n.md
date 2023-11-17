

## Find kth factor of n
- Ref: https://leetcode.com/problems/the-kth-factor-of-n/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency

### Approach

```py
import math


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factor = []
        complement = []
        for i in range(1, int(math.sqrt(n))+1):
            if n % i == 0:
                factor.append(i)
                if i != n/i:
                    complement.insert(0, n//i)

        factor = factor + complement
        if k <= len(factor):
            return factor[k-1]
        return -1


sol = Solution()
print(sol.kthFactor(12, 3))
print(sol.kthFactor(7,2))
print(sol.kthFactor(4,4))

```