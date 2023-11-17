
## Evaluate expression
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/128011/assignment/problems/46/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/045-evaluate-expression-question.png)

### Approach
- stacks

```py
class Solution:
    def evalRPN(self, A):
        stack = []

        for item in A:
            if item == "+" or item == "-" or item == "*" or item == "/":
                op1 = stack.pop()
                op2 = stack.pop()
                if item == "+":
                    stack.append(op2+op1)
                elif item == "-":
                    stack.append(op2-op1)
                elif item == "*":
                    stack.append(op2*op1)
                elif item == "/":
                    stack.append(op2//op1)
            else:
                stack.append(int(item))
        return stack[0]


sol = Solution()
print(sol.evalRPN(["2", "1", "+", "3", "*"]))
print(sol.evalRPN(["4", "13", "5", "/", "+"]))
```