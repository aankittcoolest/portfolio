
## Redundant braces
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/128011/homework/problems/274/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/045-redundant-braces-question.png)

### Approach
- stacks

```py
class Solution:
    def braces(self, A):
        stack = []

        for element in A:
            if element == ")":
                count = 0
                while stack[-1] != "(":
                    stack.pop()
                    count += 1
                stack.pop()
                if count < 2:
                    return 1
            else:
                stack.append(element)
        return 0
```