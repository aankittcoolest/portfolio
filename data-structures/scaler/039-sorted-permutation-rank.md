
## Sorted permutation rank
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/127963/assignment/problems/317/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/039-sorted-permutation-rank-question.png)

### Approach
- permuation basics

```py
class Solution:
    def findRank(self, A):

        mem = [1] * len(A)
        for i in range(2, len(A)):
            mem[i] = mem[i-1] * i % 1000003

        ln = len(A)
        ans = 0
        for i, s in enumerate(A):
            count = 0
            for j in range(i+1, len(A)):
                if ord(s) > ord(A[j]):
                    count += 1
            if count > 0:
                temp = mem[ln-i-1]
                ans += temp * count % 1000003
        return (ans+1) % 1000003


sol = Solution()
print(sol.findRank("DTNGJPURFHYEW"))
```