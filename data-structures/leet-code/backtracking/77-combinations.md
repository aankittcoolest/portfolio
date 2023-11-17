
## Combinations
- Ref: https://leetcode.com/problems/combinations/description/?envType=study-plan-v2&envId=top-interview-150


### Approach
- backtracking

```py
from typing import List


class Solution:
    def combineRecursion(self, N: int, K: int) -> List[List[int]]:

        result = []

        def combinations(n, k, temp, index, i):
            if index == k:
                result.append(temp[:])
                return
            if i == n:
                return

            temp[index] = i+1
            combinations(n, k, temp, index+1, i+1)
            combinations(n, k, temp, index, i+1)

        temp = [0] * (K)
        combinations(N, K, temp, 0, 0)
        return result

    def combineBacktrack(self, N: int, K: int) -> List[List[int]]:
        def backtrack(curr, first_num):
            if len(curr) == K:
                ans.append(curr[:])
                return

            for num in range(first_num, N+1):
                curr.append(num)
                backtrack(curr, num+1)
                curr.pop()

        ans = []
        backtrack([], 1)
        return ans


sol = Solution()
print(sol.combineBacktrack(4, 2))
print(sol.combineRecursion(4, 2))
```
