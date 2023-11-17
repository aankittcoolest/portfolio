
## Permutations
- Ref: https://leetcode.com/problems/permutations/description/?envType=study-plan-v2&envId=top-interview-150

### Approach
- backtracking

```py
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr, target, index):
            if len(curr) == target:
                ans.append(curr[:])
                return

            for i, num in enumerate(nums):
                if num in curr:
                    continue
                curr.append(num)
                backtrack(curr, target, i)
                curr.pop()
            pass

        ans = []
        target = len(nums)
        backtrack([], target, -1)
        return ans


sol = Solution()
print(sol.permute([1, 2, 3]))
```