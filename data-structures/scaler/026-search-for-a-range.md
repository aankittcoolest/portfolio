
## Search for a range
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/122344/assignment/problems/199/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/026-search-for-a-range-question.png)


### Approach
- binary search two times

```py
class Solution:
    def searchRange(self, A, B):

        def binSearchLeft():
            l = 0
            r = len(A)-1

            while l <= r:
                mid = (l+r)//2
                if A[mid] < B:
                    l = mid+1
                else:
                    r = mid-1
            return l if A[l] == B else -1

        def binSearchRight():
            l = 0
            r = len(A)-1

            while l <= r:
                mid = (l+r)//2
                if A[mid] > B:
                    r = mid-1
                else:
                    l = mid+1
            return r if A[r] == B else -1

        return [binSearchLeft(), binSearchRight()]


sol = Solution()
# sol.searchRange([5, 7, 7, 8, 8, 10, 10], 8)
# print(sol.searchRange([5, 7, 7, 8, 8, 10], 10))
print(sol.searchRange([ 4, 7, 7, 7, 8, 10, 10 ], 3))
```