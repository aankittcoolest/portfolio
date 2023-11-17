
## Balanced parenthesis
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/128011/assignment/problems/678?navref=cl_tt_lst_sl

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/045-balanced-parenthesis-question.png)

### Approach
- stacks

```py
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        stack = []
        for bracket in A:
            if bracket == "{" or bracket == "(" or bracket == "[":
                stack.append(bracket)
            elif bracket == "}":
                if len(stack) > 0 and stack.pop() == "{":
                    continue
                return 0
            elif bracket == ")":
                if len(stack) > 0 and stack.pop() == "(":
                    continue
                return 0
            elif bracket == "]":
                if len(stack) > 0 and stack.pop() == "[":
                    continue
                return 0
        if len(stack) > 0:
            return 0
        return 1


sol = Solution()
print(sol.solve("{([])}"))
print(sol.solve("(){"))
```