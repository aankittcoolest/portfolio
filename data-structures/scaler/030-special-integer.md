
## Special Integer
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/120818/homework/problems/4133/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/030-special-integer-question.png)

### Approach
- two points
- (OR) binary search

```py
class Solution:
    def solve(self, A, B):
        i = 0
        j = 0
        sum = 0
        ans = len(A)
        for element in A:
            sum += element
            j += 1
            if sum > B:
                while sum > B:
                    sum = sum - A[i]
                    i += 1
                ans = min(ans, j-i)

        return ans


sol = Solution()
print(sol.solve([1, 2, 3, 4, 5], 10))
print(sol.solve([5, 17, 100, 11], 130))
print(sol.solve([2, 24, 38, 25, 35, 33, 43, 12, 49, 35, 45, 47, 5, 33], 249))
```