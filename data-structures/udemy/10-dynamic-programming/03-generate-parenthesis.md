

## Generate parenthesis
- https://leetcode.com/problems/generate-parentheses/


### Approach
- Recursive/backtracking

```py
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l = []
        def generate(m,start,end,str):
            if start > m or end > m:
                return
            if start == end == n:
                l.append(str)

            generate(m,start+1,end,str + "(")
            if end < start:
                generate(m,start,end+1,str + ")")
        
        generate(n,0,0,"")
        return l
        

sol = Solution()
print(sol.generateParenthesis(3))
print(sol.generateParenthesis(1))

```