

## Array three pointers
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/120854/homework/problems/168/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/033-array-three-pointers-question.png)

### Approach
- pointers

```py
class Solution:
    def minimize(self, A, B, C):
        i, j, k = 0, 0, 0

        ans = float("inf")
        while i < len(A) and j < len(B) and k < len(C):
            mx = max(A[i], B[j], C[k])
            # check if i is minimum
            if A[i] <= B[j] and A[i] <= C[k]:
                ans = min(ans, mx-A[i])
                i += 1
            elif B[j] <= A[i] and B[j] <= C[k]:
                ans = min(ans, mx-B[j])
                j += 1
            elif C[k] <= A[i] and C[k] <= B[j]:
                ans = min(ans, mx-C[k])
                k += 1
        return ans



sol = Solution()
print(sol.minimize([1, 4, 10], [2, 15, 20], [10, 12]))
```
