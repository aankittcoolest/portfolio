
## Maximum and minimum magic
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/120695/homework/problems/8644/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/024-maximum-and-minimum-magic-question.png)

### Approach
- sorting
- figure out how to calculate maximum and minimum

```py
class Solution:
    def solve(self, A):
        A.sort()
        mx_sum = 0
        mn_sum = 0
        mod = 10 ** 9 + 7
        for i in range(len(A)//2):
            mx_sum = (mx_sum % mod + abs(A[i]-A[len(A)-i-1]) % mod) % mod

        for i in range(0, len(A), 2):
            mn_sum = (mn_sum %mod +  abs(A[i]-A[i+1]) % mod) % mod
        return [mx_sum, mn_sum]


sol = Solution()
print(sol.solve([3, 11, -1, 5]))
```
