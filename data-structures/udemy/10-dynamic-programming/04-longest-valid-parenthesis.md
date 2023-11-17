

## Longest valid parenthesis
- Ref: https://leetcode.com/problems/longest-valid-parentheses/


### Approach
- TODO: Solve using dynaminc programming
- Here we try to solve it using simpler approach

```py
class Solution:

    def longestValidParentheses(self, s: str) -> int:
        open_count = 0
        close_count = 0
        max_valid_substr_len = 0
        valid_substr_len = 0
        for bracket in s:
            if bracket == "(":
                open_count += 1

            elif close_count <= open_count:
                close_count += 1

            # Here close count will come resulting in creating more closes
            if close_count > 0 and open_count == close_count:
                if max_valid_substr_len < close_count * 2:
                    max_valid_substr_len = close_count * 2
            if close_count > open_count:
                open_count = 0
                close_count = 0

        open_count=0
        close_count=0

        for i in range(len(s)-1,-1,-1):
            if s[i] == ")":
                close_count += 1

            elif open_count <= close_count:
                open_count += 1

            # Here close count will come resulting in creating more closes
            if close_count > 0 and open_count == close_count:
                if max_valid_substr_len < close_count * 2:
                    max_valid_substr_len = close_count * 2

            if open_count > close_count:
                open_count = 0
                close_count = 0


        return max_valid_substr_len




sol = Solution()
# print(sol.longestValidParentheses(")()())()()("))
# print(sol.longestValidParentheses("()"))
# print(sol.longestValidParentheses("()(()"))
# print(sol.longestValidParentheses("(((("))
# print(sol.longestValidParentheses(")(()(()(((())(((((()()))((((()()(()()())())())()))()()()())(())()()(((()))))()((()))(((())()((()()())((())))(())))())((()())()()((()((())))))((()(((((()((()))(()()(())))((()))()))())"))
print(sol.longestValidParentheses("(()"))
# print(sol.longestValidParentheses(")()())"))
# print(sol.longestValidParentheses("()(()"))
# print(sol.longestValidParentheses(")))(("))
```