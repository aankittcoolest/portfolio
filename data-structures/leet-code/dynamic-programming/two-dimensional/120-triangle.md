## Triange
- Ref: https://leetcode.com/problems/triangle/description/?envType=study-plan-v2&envId=top-interview-150


### Approach
- Dynamic Programming

```py
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle)+1)

        for row in triangle[::-1]:
            for i, n in enumerate(row):
                dp[i] = n + min(dp[i], dp[i+1])
        return dp[0]


sol = Solution()
print(sol.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
```