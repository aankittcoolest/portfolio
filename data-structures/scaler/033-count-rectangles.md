
## Count rectangles
- Ref:https://www.scaler.com/academy/mentee-dashboard/class/120854/homework/problems/4115/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/033-count-rectangles-question.png)


### Approach
- two pointers

```py
class Solution:
    def solve(self, A, B):
        l = 0
        r = len(A)-1
        count = 0
        while l <= len(A)-1 and r >= 0:
            if A[l] * A[r] < B:
                count += (r+1)
                l += 1
            else:
                r = r - 1
        return count % 1000000007


sol = Solution()
print(sol.solve([1, 2, 3, 4, 5, 6, 8, 10], 35))
# print(sol.solve([1, 2, 3, 4, 5, 6, 8, 10], 25))
# print(sol.solve([1, 2], 5))

```