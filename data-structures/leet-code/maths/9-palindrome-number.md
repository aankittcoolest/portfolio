
## Check palindrome number
- Ref: https://leetcode.com/problems/palindrome-number/description/?envType=study-plan-v2&envId=top-interview-150

### Approach
- maths

```py
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversedNum = 0

        while x > reversedNum:
            digit = x % 10
            reversedNum = (reversedNum * 10) + digit
            x = x//10

        if x == reversedNum or x == reversedNum//10:
            return True

        return False


sol = Solution()
# print(sol.isPalindrome(12321))
# print(sol.isPalindrome(10))
print(sol.isPalindrome(23))
```