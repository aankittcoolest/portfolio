

## Minimum swaps to group 1's together
- Ref: https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency

### Approach
- Sliding window

```py
from typing import List


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        maxOnesCount = 0

        for i in data:
            if i == 1:
                maxOnesCount += 1

        if maxOnesCount == 0:
            return 0

        ans = -1
        onesCount = 0

        # ones count in start window
        for i in range(0, maxOnesCount):
            if data[i] == 1:
                onesCount += 1
        ans = onesCount

        j = 0
        # sliding window
        for i in range(maxOnesCount, len(data)):
            if data[i] == 1 and data[j] == 0:
                onesCount += 1
            if data[i] == 0 and data[j] == 1:
                onesCount -= 1
            if ans < onesCount:
                ans = onesCount
            j += 1

        return maxOnesCount-ans


sol = Solution()
print(sol.minSwaps([1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1]))
print(sol.minSwaps([1, 0, 0]))

```