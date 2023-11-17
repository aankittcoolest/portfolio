

## Coin change
- Ref: https://leetcode.com/problems/coin-change/?envType=study-plan-v2&envId=top-interview-150


### Approach
- Dynamic programming

```py
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0

        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])

        return dp[amount] if dp[amount] <= amount else -1


sol = Solution()
print(sol.coinChange([1, 5, 2], 11))
print(sol.coinChange([2], 3))
print(sol.coinChange([4],4))
print(sol.coinChange([1],0))
print(sol.coinChange([1,5,2],357))
print(sol.coinChange([186,419,83,408],6249))

```