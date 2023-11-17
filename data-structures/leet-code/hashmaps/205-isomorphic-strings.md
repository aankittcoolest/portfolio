## Isomorphic strings
- Ref: https://leetcode.com/problems/isomorphic-strings/description/?envType=study-plan-v2&envId=top-interview-150

### Approach
- hashmap


```py
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d = {}
        for i, _ in enumerate(s):
            if d.get(s[i]) is not None and d[s[i]] != t[i]:
                return False
            d[s[i]] = t[i]

        d = {}
        for i, _ in enumerate(t):
            if d.get(t[i]) is not None and d[t[i]] != s[i]:
                return False
            d[t[i]] = s[i]
        return True


sol = Solution()
print(sol.isIsomorphic("egg", "add"))
print(sol.isIsomorphic("foo", "bar"))
print(sol.isIsomorphic("badc", "baba"))
print(sol.isIsomorphic("paper", "title"))
```