
## Merge array to turn it into palindrome
- Ref: https://leetcode.com/problems/merge-operations-to-turn-array-into-a-palindrome/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency

### Approach

```py
from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        i = 0
        j = len(nums)-1

        opCount = 0
        while i < j:
            if nums[i] > nums[j]:
                nums[j-1] = nums[j] + nums[j-1]
                nums[j] = None
                j = j-1
                opCount += 1
            elif nums[i] < nums[j]:
                nums[i+1] = nums[i] + nums[i+1]
                nums[i] = None
                i = i+1
                opCount += 1
            else:
                i = i + 1
                j = j - 1
        return opCount



sol = Solution()
print(sol.minimumOperations([4, 3, 2, 1, 2, 3, 1]))
print(sol.minimumOperations([1, 2, 3, 4]))
```