
## Subarray with given sum
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/120854/assignment/problems/4116/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/031-subarray-with-given-sum-question.png)

### Approach
- two pointers

```py
class Solution:
    def solve(self, A, B):
        i, j = 0, 0
        sum = 0

        for k in range(0, len(A)):
            sum += A[j]
            j += 1
            if sum == B:
                return A[i:j]
            while i<j and sum > B:
                sum -= A[i]
                i += 1
                if sum == B:
                    return A[i:j]
                if sum < B:
                    break
        return [-1]


sol = Solution()
# print(sol.solve([1, 2, 3, 4, 5], 5))
# print(sol.solve([1], 5))
# print(sol.solve([1, 2], 3))
print(sol.solve([5, 10, 20, 100, 105], 110))
# print(sol.solve([42, 9, 38, 36, 48, 33, 36, 50, 38,
#       8, 13, 37, 33, 38, 17, 25, 50, 50, 41], 100))

```