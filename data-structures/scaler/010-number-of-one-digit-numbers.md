
## Number of one digit numbers
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/81683/homework/problems/4099?navref=cl_tt_nv

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/010-number-of-one-digit-numbers-question.png)

### Approach

```py
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        i = 1
        total = 0
        while i <= A:
            count = (A//(i * 10)) * i + min(max(A % (i * 10) - (i-1), 0), i)
            total += count
            i = i * 10
        return total

sol = Solution()
# print(sol.solve(11))
print(sol.solve(452))
# print(sol.solve(21))
# print(sol.solve(10))
```