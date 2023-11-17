
## Add two binary numbers
- Ref: https://leetcode.com/problems/add-binary/?envType=study-plan-v2&envId=top-interview-150

### Approach
- Simply loop through each character of binary number and do modulo 2 addition.

```py
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        a, b = a[::-1], b[::-1]

        for i in range(max(len(a), len(b))):
            digitA = ord(a[i])-ord("0") if i < len(a) else 0
            digitB = ord(b[i])-ord("0") if i < len(b) else 0

            sum = digitA + digitB + carry
            ch = sum % 2
            res = str(ch) + res
            carry = sum//2

        if carry:
            res = str(carry) + res
        return res


sol = Solution()
print(sol.addBinary("11", "1"))

```