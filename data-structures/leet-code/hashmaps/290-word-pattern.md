
## Word pattern
- Ref:

### Approach
- hashmap

```py
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern):
            return False

        d = {}

        i = 0
        for c in pattern:
            if d.get(c) is not None and d[c] != "$" + words[i]:
                return False
            if d.get("$" + words[i]) is not None and d["$" + words[i]] != c:
                return False
            d[c] = "$" + words[i]
            d["$" + words[i]] = c
            i += 1

        return True


sol = Solution()
print(sol.wordPattern("abba", "dog cat cat dog"))
print(sol.wordPattern("abc", "a b c"))
print(sol.wordPattern("abba", "dog dog dog dog"))
print(sol.wordPattern("abba", "dog cat cat cat"))
print(sol.wordPattern("abba", "dog cat cat fish"))
```


