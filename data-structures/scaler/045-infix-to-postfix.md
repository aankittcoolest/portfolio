
## Infix to postfix
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/128011/homework/problems/4353/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/045-infix-to-postfix-question.png)

### Approach
- stacks

```py
class Solution:
    def solve(self, A):

        def getPrecedence(ch):
            if ch == "^":
                return 3
            elif ch == "*" or ch == "/":
                return 2
            elif ch == "+" or ch == "-":
                return 1
            return 0

        stack = []
        output = ""
        for item in A:
            if item == "(":
                stack.append("(")
            elif item == "^" or item == "/" or item == "*" or item == "+" or item == "-":
                while len(stack) > 0 and getPrecedence(stack[-1]) >= getPrecedence(item):
                    output += stack.pop()
                stack.append(item)
            elif item == ")":
                while stack[-1] != "(":
                    output += stack.pop()
                stack.pop()
            else:
                output += item

        while len(stack) > 0:
            output += stack.pop()

        return output
```