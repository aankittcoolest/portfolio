
## Bitwise AND of numbers range
- Ref: https://leetcode.com/problems/bitwise-and-of-numbers-range/editorial/?envType=study-plan-v2&envId=top-interview-150

### Approach
- bit-manipulation
- Brian Kerninghan's algorithm

```py
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count = 0
        while left != right:
            left >>= 1
            right >>= 1
            count+= 1
        return left << count


sol = Solution()
# print(sol.rangeBitwiseAnd(5, 7))
# print(sol.rangeBitwiseAnd(16, 19))
print(sol.rangeBitwiseAnd(17, 19))

```