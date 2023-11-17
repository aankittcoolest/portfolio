
## Reverse bits
- Ref: https://leetcode.com/problems/reverse-bits/description/?envType=study-plan-v2&envId=top-interview-150


### Approach
- Bit manipulation
- Logical "&" operation gives the current bit of the number
- To set the bit we do logical OR operation "|"
- Do left and right shifts

```py
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = n >> i & 1
            res = res | bit << (31-i)
        return res

sol = Solution()
print(sol.reverseBits(43261596))
```

