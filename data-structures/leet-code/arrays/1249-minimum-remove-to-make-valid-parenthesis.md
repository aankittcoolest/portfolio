
## Minimum remove to make valid parenthesis
- Ref: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/


### Approach
- stack

```py
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        def deleteInvalidClosing(st, start,end) -> str:
            balance = 0
            res = []
            for c in st:
                if c  == start:
                    balance += 1
                elif c == end:
                    if balance == 0:
                        continue
                    balance -= 1
                res.append(c)
            return "".join(res)
        
        out = deleteInvalidClosing(s,"(", ")")
        out = deleteInvalidClosing(out[::-1],")", "(")
        return out[::-1]
            
                

                



sol = Solution()
print(sol.minRemoveToMakeValid("lee(t(c)o)de)"))
print(sol.minRemoveToMakeValid("a)b(c)d"))
print(sol.minRemoveToMakeValid("())()((("))
```