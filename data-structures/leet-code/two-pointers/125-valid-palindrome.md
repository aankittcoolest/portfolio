
## Valid palindrome
- Ref: https://leetcode.com/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150

### Approach
- Two pointers

```py
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = 0
        r = len(s)-1

        while l < r:
            if s[l].isalnum() == False:
                l += 1
            elif s[r].isalnum() == False:
                r -= 1
            elif s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True


sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))
print(sol.isPalindrome("race a car"))
print(sol.isPalindrome(" "))
print(sol.isPalindrome("0P"))
```


