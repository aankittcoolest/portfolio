
## Aggressive cows
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/120818/assignment/problems/4129?navref=cl_tt_lst_sl

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/030-aggressive-cows-question.png)

### Approach
- binary search

```py
class Solution:
    def solve(self, A, B):

        def check(mid):
            cows_position = A[0]
            cows = B - 1
            for i in range(1, len(A)):
                if cows == 0:
                    return True
                if A[i] - cows_position >= mid:
                    cows -= 1
                    cows_position = A[i]
            if cows == 0:
                return True
            return False

        A.sort()
        l = 0
        r = A[len(A)-1]
        ans = 1
        while l <= r:
            mid = (l+r)//2
            if check(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans


sol = Solution()
# print(sol.solve([1, 2, 4, 8, 9], 3))
# print(sol.solve([1, 2, 3, 4, 5], 3))
print(sol.solve([1, 2], 2))
```
