
## Subarray sum equal to k
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/120870/assignment/problems/4827/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/032-subarray-sum-equal-to-k-question.png)


### Approach
- hashmap
- prefix-sum

```py
class Solution:
    def solve(self, A, B):
        psum = [0] * len(A)
        psum[0] = A[0]
        d = {}
        ans = 0

        sum = 0
        for element in A:
            sum += element
            if sum == B:
                ans += 1
            if d.get(sum-B):
                ans += d[sum-B]
            if d.get(sum):
                d[sum] += 1
            else:
                d[sum] = 1

        return ans


sol = Solution()
print(sol.solve([1, 1, 2, 1, 0, 1], 2))
# print(sol.solve([1, 1, 2, 2, 2, 1, 0, 1], 2))
# print(sol.solve([13,9,19,-9,-19,14,-15],15))
# print(sol.solve([-2, 16, -12, 5, 7, -1, 2, 12, 11], 17))
print(sol.solve([-20,-13,4,2,18,-17,17],11))
```



