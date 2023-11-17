
## Number of 1 bits
- Ref

### Approach
- bit-manipulation
- Do "&" with each bit to get the set bit

```py
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            bit = (n >> i) & 1
            if bit:
                count += 1
        return count
        
sol = Solution()
sol.hammingWeight(11)
```