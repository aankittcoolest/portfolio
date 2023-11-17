
## Distinct numbers in window
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/121022/assignment/problems/333/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/031-hashing-distinct-numbers-in-window-question.png)

### Approach
- hashing

```py
class Solution:
    def dNums(self, A, B):
        d = {}
        ans = []
        for i in range(len(A)):
            if i >= B:
                ans.append(len(d))
                # remove this element
                if d.get(A[i-B]) > 1:
                    d[A[i-B]] = d[A[i-B]] - 1
                else:
                    del d[A[i-B]]
            # add ith element
            if d.get(A[i]) is not None:
                d[A[i]] = d[A[i]] + 1
            else:
                d[A[i]] = 1
        ans.append(len(d))
        return ans


sol = Solution()
print(sol.dNums([1, 2, 1, 3, 4, 3], 3))
print(sol.dNums([1, 1, 2, 2], 1))
```