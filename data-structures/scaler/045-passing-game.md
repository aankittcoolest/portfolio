
## Passing game
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/128011/assignment/problems/1064/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/045-passing-game-question.png)

### Approach
- stacks

```py
class Solution:
    def solve(self, A, B, C):
        stack = []
        stack.append(B)
        for element in C:
            if element == 0:
                stack.pop()
            else:
                stack.append(element)
            A -= 1
            if A == 0:
                return stack[-1]
        return stack[-1]


sol = Solution()
print(sol.solve(10, 23, [86, 63, 60, 0, 47, 0, 99, 9, 0, 0]))
print(sol.solve(1, 1, [2]))
```