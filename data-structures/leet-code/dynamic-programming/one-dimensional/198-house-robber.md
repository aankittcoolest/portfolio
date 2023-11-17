
## House Robber
- Ref: https://leetcode.com/problems/house-robber/description/?envType=study-plan-v2&envId=top-interview-150


### Approach
- dynamic-programming

```py
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        def robRecursive(sum, n):
            if len(n) == 0:
                return sum
            return max(robRecursive(sum + n[0], n[2:]), robRecursive(sum, n[1:]))

        def robRecursiveMemo(sum, n, index, dp):
            print(dp)
            if index > len(n)-1:
                return sum
            if dp[index]:
                return dp[index]
            else:
                dp[index] = max(robRecursiveMemo(
                    sum + n[index], n, index + 2, dp), robRecursiveMemo(sum, n, index + 1, dp))
            return dp[index]

        # dp = [0] * len(nums)
        # print(robRecursiveMemo(0, nums, 0, dp))

        def robDP(n):
            rob1,rob2 = 0,0

            for house in n:
               temp1 = max(house + rob1,rob2)
               rob1 = rob2
               rob2 = temp1
            
            return rob2

        return robDP(nums)

        




sol = Solution()
print(sol.rob([2, 7, 9, 3, 1]))
# print(sol.rob([2]))
# print(sol.rob([2, 7, 2]))
# print(sol.rob([2, 1, 1, 2]))
```