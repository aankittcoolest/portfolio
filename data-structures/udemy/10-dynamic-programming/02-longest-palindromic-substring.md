## Longest palindromic substring
Ref: https://leetcode.com/problems/longest-palindromic-substring/


```py
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ## create 2D matrix
        m = []
        for i,s1 in enumerate(s):
            l = []
            sum = ""
            for j,s2 in enumerate(s):
                if j < i:
                    l.append(None)
                elif j == i:
                    sum = s1
                    l.append(self.checkPalindrome(sum))
                else:
                    sum = sum  + s2
                    l.append(self.checkPalindrome(sum))
            m.append(l)

        j=0
        max = -1
        out = ""
        for i in range(len(m)):
            for j in range(len(m)):
                if m[i][j] == True:
                    if max < len(s[i:j+1]):
                        max = len(s[i:j+1])
                        out = s[i:j+1]
        return out

    def checkPalindrome(self,s):
        if len(s) == 1:
            return True
        # string is even
        if len(s)%2 == 0:
            if s[:len(s)//2] == s[len(s)//2:][::-1]:
                return True
        elif s[:len(s)//2] == s[len(s)//2 + 1:][::-1]:
                return True
        return False




sol = Solution()
print(sol.longestPalindrome("cbbd"))
print(sol.longestPalindrome("aacabdkacaa"))
print(sol.longestPalindrome("babad"))
print(sol.longestPalindrome("a"))
# print(sol.longestPalindrome("aba"))
# print(sol.longestPalindrome("abba"))
# print(sol.longestPalindrome("ababa"))
# print(sol.longestPalindrome("ank"))
# print(sol.checkPalindrome("aabca"))
```