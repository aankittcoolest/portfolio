
## Ransom note
- Ref: https://leetcode.com/problems/ransom-note/?envType=study-plan-v2&envId=top-interview-150


### Approach
- hashmap

```py
import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        d = collections.Counter(magazine)

        for c in ransomNote:
            if d[c] <= 0:
                return False
            d[c] -= 1
        return True


sol = Solution()
print(sol.canConstruct("aa", "aab"))
print(sol.canConstruct("aa", "ab"))
```
