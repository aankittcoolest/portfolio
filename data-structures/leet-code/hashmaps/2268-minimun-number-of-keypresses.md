
## Minimum number of keypress
- Ref:https://leetcode.com/problems/minimum-number-of-keypresses/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency

### Approach
- hashmaps

```py
class Solution:
    def minimumKeypresses(self, s: str) -> int:
        d = {}
        for k in s:
            if d.get(k):
                d[k] += 1
            else:
                d[k] = 1
        d = dict(sorted(d.items(), key=lambda item: item[1],reverse=True))

        ans = 0
        increase = 1
        count = 9
        i = 1
        for key in d.keys():
            if i > count:
                count += count
                increase += 1
            d[key] = increase
            i += 1
        
        for k in s:
            ans += d.get(k)

        return ans
    
sol = Solution()
sol.minimumKeypresses("abcdefghijklabzz")
sol.minimumKeypresses("abcdefghijkl")
print(sol.minimumKeypresses("aaaaaaaabcdefgggghijkllllllllllmmmnoppponono"))
```

