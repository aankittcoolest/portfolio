
## Painter partition problem
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/120818/assignment/problems/271/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/030-painter-partition-problem-question.png)


### Approach
- binary search


```py
class Solution:
    def isPossibile(self, A, B, C, bucket):
        sum = 0
        for element in C:
            sum += (element * B)
            if sum > bucket:
                sum = (element * B)
                A -= 1
        A -= 1
        if A >= 0:
            return True
        return False

    def paint(self, A, B, C):
        best = max(C) * B
        worst = sum(C) * B

        ans = worst
        while best <= worst:
            mid = (best + worst)//2
            if self.isPossibile(A, B, C, mid):
                ans = min(ans, mid)
                worst = mid - 1
            else:
                best = mid + 1
        return ans % 10000003


sol = Solution()
# sol.paint(2, 1, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(sol.paint(3, 10, [185, 186, 938, 558, 655, 461, 441, 234, 902, 681]))
# sol.paint(10, 1, [1, 8, 11, 3])
```