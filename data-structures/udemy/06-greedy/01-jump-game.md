## Jump to reach the last index of array
- Ref: https://leetcode.com/problems/jump-game/

### Tags
- Greedy Approach
- Dynamic programming


### Approach
- Greedy approach: Start with best local solution at given point in time to reach the best optimal global solution.
- TODO: Solve the problem using dynamic programming

```py
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # The goal is to reach the end of the array, so we start from there as the goalpost
        goal = len(nums) - 1

        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= goal:
                goal = i
        
        return True if goal == 0 else False


sol = Solution()
print(sol.canJump([2, 3, 1, 1, 4])) # True
print(sol.canJump([3, 2, 1, 0, 4])) # False

```