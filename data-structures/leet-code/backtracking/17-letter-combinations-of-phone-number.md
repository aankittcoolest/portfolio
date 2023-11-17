## Letter combinations of phone number
- Ref: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/?envType=study-plan-v2&envId=top-interview-150

### Approach
- backtracking

```py
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        stack1 = []
        stack2 = []
        for i in digits[len(digits)-1]:
            comb = d[i]
            for c in comb:
                stack2.append(c)

        for i in range(len(digits)-2, -1, -1):
            comb = d[digits[i]]
            while stack2:
                element = stack2.pop()
                for c in comb:
                    stack1.append(c + element)
            stack2 = stack1
            stack1 = []
        return stack2


sol = Solution()
# print(sol.letterCombinations("232"))
# print(sol.letterCombinations("2"))
print(sol.letterCombinations(""))
```