
## Plus one
- Ref: https://leetcode.com/problems/plus-one/description/?envType=study-plan-v2&envId=top-interview-150

### Approach
- maths

```py
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(len(digits)-1, -1, -1):
            if i == len(digits)-1:
                sum = digits[i] + 1 + carry
            else:
                sum = digits[i] + carry

            if sum >= 10:
                carry = 1
                digits[i] = sum % 10
            else:
                carry = 0
                digits[i] = sum % 10
        print(carry)
        if carry:
            digits.insert(0, carry)
        return digits


sol = Solution()
print(sol.plusOne([1, 2, 9, 0]))
print(sol.plusOne([9, 9]))
```
