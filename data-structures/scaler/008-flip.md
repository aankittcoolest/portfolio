
## Flip
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/81677/homework/problems/329/?navref=cl_pb_nv_tb


## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/008-flip-question.png)

### Approach
- kadane algorithm
- change 1 to -1 and calculate max sum.
- If current_sum < 0, return it back to zero.
- Maintain two pointers (l,r)

```py
class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        sum = 0
        maxSum = 0
        l = 0
        r = 0
        ans = []
        for i, c in enumerate(A):
            if c == "1":
                sum = sum - 1
            else:
                sum = sum + 1
            if sum > maxSum:
                maxSum = sum
                ans = [l+1, r+1]
            if sum < 0:
                sum = 0
                l = i + 1
                r = i + 1
            else:
                r = r + 1
        return ans


sol = Solution()
# print(sol.flip("0110010001000"))
print(sol.flip("010"))
print(sol.flip("111"))
```

