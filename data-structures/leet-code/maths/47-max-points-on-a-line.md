
## Max points on a line
- Ref: https://leetcode.com/problems/max-points-on-a-line/description/?envType=study-plan-v2&envId=top-interview-150


### Approach
- maths

```py
from typing import List
import collections


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 1

        for i in range(len(points)):
            p1 = points[i]
            count = collections.defaultdict(int)
            for j in range(i+1, len(points)):
                p2 = points[j]
                if p1[0] == p2[0]:
                    slope = float("inf")
                else:
                    slope = (p2[1] - p1[1])/(p2[0]-p1[0])
                count[slope] += 1
                res = max(res, count[slope]+1)
        return res


sol = Solution()
print(sol.maxPoints([[1,1],[2,2],[3,3]]))
print(sol.maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))
```
