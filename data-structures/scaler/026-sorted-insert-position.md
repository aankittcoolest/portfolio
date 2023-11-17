
## Sorted insert position
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/122344/assignment/problems/204/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/026-sorted-insert-position-question.png)

### Approach
- binary search

```py
class Solution:
    def searchInsert(self, A, B):
        l = 0
        r = len(A)-1
        while l <= r:
            mid = (l+r)//2
            if A[mid] == B:
                return mid
            elif A[mid] < B:
                l = mid+1
            else:
                r = mid-1
        if l == len(A):
            return r
        return l


sol = Solution()
# print(sol.searchInsert([1, 3, 5, 6],5))
# print(sol.searchInsert([1, 4, 9], 3))
print(sol.searchInsert([1, 4, 9], 0))
print(sol.searchInsert([1, 4, 9], 3))
print(sol.searchInsert([1, 4, 9], 13))
```