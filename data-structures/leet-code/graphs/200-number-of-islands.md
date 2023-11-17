
## Number of islands
- Ref: https://leetcode.com/problems/number-of-islands/description/?envType=study-plan-v2&envId=top-interview-150


### Approach
- graph theory
- bfs

```py
from typing import List
import collections


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                r, c = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    if ((r+dr) in range(rows) and
                        (c + dc) in range(cols) and
                        grid[r+dr][c+dc] == "1" and
                            (r+dr, c+dc) not in visited):
                        q.append((r+dr, c+dc))
                        visited.add((r+dr, c+dc))

            pass

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands


sol = Solution()
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

print(sol.numIslands(grid))

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(sol.numIslands(grid))
```
