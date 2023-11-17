
## Trapping rain water
- Ref: https://leetcode.com/problems/trapping-rain-water/description/?envType=study-plan-v2&envId=top-interview-150


### Approach
- max-min

```py
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        rpass = [0] * len(height)
        lpass = [0] * len(height)
        for i in range(1, len(height)):
            rpass[i] = max(height[i-1], rpass[i-1])

        for i in range(len(height)-2, -1, -1):
            lpass[i] = max(height[i+1], lpass[i+1])

        sum = 0
        for i in range(len(height)):
            ans = (min(rpass[i], lpass[i]) - height[i])
            if ans > 0:
                sum += ans

        return sum


sol = Solution()
print(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
```
