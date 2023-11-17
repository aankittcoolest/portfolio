
## Longest common subsequence
- Ref: https://leetcode.com/problems/longest-increasing-subsequence/?envType=study-plan-v2&envId=top-interview-150


### Approach
- dynaminc-programming

```py
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        out = 1

        for i in range(len(nums)-2, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1+dp[j])

            if out < dp[i]:
                out = dp[i]

        return out


sol = Solution()
print(sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(sol.lengthOfLIS([0, 1, 0, 3, 2, 3]))
print(sol.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))
print(sol.lengthOfLIS([4, 10, 4, 3, 8, 9]))

```