
## Double character trouble
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/128011/assignment/problems/968/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/045-double-character-trouble-question.png)

### Approach
- stacks

```py
class Solution:
    def solve(self, A):
        ans = []

        for a in A:
            if len(ans) == 0:
                ans.append(a)
            elif ans[-1] == a:
                ans.pop()
            else:
                ans.append(a)

        return "".join(ans)

sol = Solution()
print(sol.solve("abccbc"))
```