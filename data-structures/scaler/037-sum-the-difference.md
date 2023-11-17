
## Sum the difference
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/121010/assignment/problems/453/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/037-sum-the-difference-question.png)

### Approach
- contribution technique

```py
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        pow_two = [0] * n
        pow_two[0] = 1

        for i in range(1, n):
            pow_two[i] = pow_two[i-1] * 2

        A.sort()

        ans = 0
        for i, element in enumerate(A):
            ans += pow_two[i] * element - pow_two[len(A)-1-i] * element
            ans = ans % (10**9 + 7)
        return ans


sol = Solution()
print(sol.solve([1, 2]))
print(sol.solve([3, 5, 10]))
```