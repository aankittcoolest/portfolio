
## Maximum height of staircase
- Ref:https://www.scaler.com/academy/mentee-dashboard/class/120942/homework/problems/4101/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/028-maximum-height-of-staircase-question.png)


### Approach
- Binary search

```py
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        l = 1
        r = A
        mid = 0

        while l <= r:
            mid = (l + r)//2
            comp = (mid * (mid+1))//2
            if comp == A:
                return mid
            if comp > A:
                r = mid - 1
            else:
                l = mid + 1
        comp = (mid * (mid+1))//2
        return mid if comp <= A else mid - 1


sol = Solution()
# print(sol.solve(10))
# print(sol.solve(20))
print(sol.solve(0))
```
