
## Three sum
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/120854/assignment/problems/165/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/033-three-sum-question.png)

### Approach
- two pointers

```py
class Solution:
    def threeSumClosest(self, A, B):
        A.sort()
        cur = float("inf")
        for i in range(0, len(A)-2):
            a = i
            b = i+1
            c = len(A)-1
            while b < c:
                sum = A[a] + A[b] + A[c]
                if abs(sum-B) < abs(cur-B):
                    cur = sum

                if sum > B:
                    c = c - 1
                elif sum < B:
                    b = b + 1
                elif sum == B:
                    return sum

        return cur


sol = Solution()
# print(sol.threeSumClosest([-1, 2, 1, -4], 1))
print(sol.threeSumClosest([-5, 1, 4, -7, 10, -7, 0, 7, 3, 0, -2, -5, -3, -6, 4, -7, -8, 0, 4, 9, 4, 1, -8, -6, -6,
      0, -9, 5, 3, -9, -5, -9, 6, 3, 8, -10, 1, -2, 2, 1, -9, 2, -3, 9, 9, -10, 0, -9, -2, 7, 0, -4, -3, 1, 6, -3], -1))
```
