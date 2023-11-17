
## Two sum
- Ref: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/?envType=study-plan-v2&envId=top-interview-150

### Approach
- Two pointers

```py
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1

        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            if numbers[l] + numbers[r] < target:
                l += 1
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]

        return [-1]


sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
print(sol.twoSum([2, 3, 4], 6))
print(sol.twoSum([-1, 0], -1))

```