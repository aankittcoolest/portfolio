
## Simplify path
- Ref: https://leetcode.com/problems/simplify-path/description/?envType=study-plan-v2&envId=top-interview-150


### Approach
- stacks

```py
class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        dir = ""
        for portion in path.split("/"):
            if portion == "..":
                if st:
                    st.pop()
            elif portion == "." or not portion:
                continue
            else:
                st.append(portion)
        
        return "/" + "/".join(st)
```