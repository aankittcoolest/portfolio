

## Optimal partition of string
- Ref: https://leetcode.com/problems/optimal-partition-of-string/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency

### Approach
- hashmaps

```py
class Solution:
    def partitionString(self, s: str) -> int:
        dict = {}
        count = 1
        for i in s:
            if dict.get(i) is not None:
                count += 1
                dict = {}
            dict[i] = True
        return count


sol = Solution()
print(sol.partitionString("abacaba"))
```
