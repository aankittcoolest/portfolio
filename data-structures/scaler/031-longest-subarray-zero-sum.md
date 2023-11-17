
## Longest subarray zero sum
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/121022/homework/problems/27742/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/031-longest-subarray-zero-sum-question.png)


### Approach
- psum
- hasmap

```py
class Solution:
    def solve(self, A):
        psum = [0] * len(A)
        psum[0] = A[0]

        for i in range(1, len(A)):
            psum[i] = A[i] + psum[i-1]
            if psum[i] == 0:
                return i+1

        d = {}
        ans = 0
        for i, element in enumerate(psum):
            if d.get(element) is None:
                d[element] = i
            else:
                ans = max(ans, i-d[element])

        return ans


sol = Solution()
# print(sol.solve([1, -2, 1, 2]))
# print(sol.solve([3, 2, -1]))
# print(sol.solve([4, 3, 2, 5, -8, 2, -4, 3]))
# print(sol.solve([9, -20, -11, -8, -4, 2, -12, 14, 1]))

# print(sol.solve([-10, 8, -2, 12, -1, -18, 18]))
print(sol.solve([11,3,0,2,7,-11,4,-14,-14]))
```
