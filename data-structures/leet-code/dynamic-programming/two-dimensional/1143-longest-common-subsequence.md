
## Longest common subsequence
- Ref:https://leetcode.com/problems/longest-common-subsequence/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency


### Approach
- Dynamic Programming

```py
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]

        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    # add diagnol
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    # get maximum of right and bottom
                    dp[i][j] = max(dp[i+1][j],dp[i][j+1])

        return dp[0][0]


sol = Solution()
print(sol.longestCommonSubsequence("abcde", "acef"))
print(sol.longestCommonSubsequence("abc", "abc"))
print(sol.longestCommonSubsequence("abc", "def"))
print(sol.longestCommonSubsequence("psnw", "vozsh"))
```