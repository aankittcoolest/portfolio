
## Minimum path sum
- Ref: https://leetcode.com/problems/minimum-path-sum/description/?envType=study-plan-v2&envId=top-interview-150

### Approach
- Dynamic Progamming

```py
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[-1 for _ in range(len(grid[0]) + 1)] for _ in range(len(grid) + 1)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                dp[i][j] = grid[i][j]

        for i in range(len(grid)-1, -1, -1):
            for j in range(len(grid[0])-1, -1, -1):
                if dp[i+1][j] == -1 and dp[i][j+1] == -1:
                    dp[i][j] = dp[i][j]
                elif dp[i+1][j] == -1:
                    dp[i][j] = dp[i][j+1] + dp[i][j]
                elif dp[i][j+1] == -1:
                    dp[i][j] = dp[i+1][j]+dp[i][j]
                else:
                    dp[i][j] = min(dp[i+1][j] + dp[i][j],
                                   dp[i][j+1] + dp[i][j])

        return dp[0][0]


sol = Solution()
# print(sol.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
print(sol.minPathSum([[1,2,3],[4,5,6]]))
```
