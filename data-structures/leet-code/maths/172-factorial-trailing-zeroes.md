
## Factorial trailing zeroes
- Ref: https://leetcode.com/problems/factorial-trailing-zeroes/description/?envType=study-plan-v2&envId=top-interview-150

### Approach
- maths

```py
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n > 0:
            count += n//5
            n = n//5
        return count

    
sol = Solution()
print(sol.trailingZeroes(50))
print(sol.trailingZeroes(5))
print(sol.trailingZeroes(25))
```