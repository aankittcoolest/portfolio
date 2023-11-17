
## Rotated sorted array search
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/120894/assignment/problems/203/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/029-rotated-sorted-array-search-question.png)


### Approach
- binary search

```py
class Solution:
    def search(self, A, B):

        def findPivot():
            l = 0
            r = len(A)-1
            while l <= r:
                mid = (l+r)//2
                if A[mid-1] > A[mid]:
                    return (mid-1, mid)
                # move left
                elif A[mid] < A[0]:
                    r = mid-1
                # move right
                else:
                    l = mid+1

        def findElement(C):
            l = 0
            r = len(C)-1
            while l <= r:
                mid = (l+r)//2
                if C[mid] == B:
                    return mid
                # move left
                if C[mid] > B:
                    r = mid-1
                # move right
                else:
                    l = mid+1
            return -1

        pivot = findPivot()
        if pivot:
            result = findElement(A[0:pivot[0]+1])
            if result != -1:
                return result
            result = findElement(A[pivot[1]:])
            if result != -1:
                return pivot[1] + result
        else:
            result = findElement(A)
            if result != -1:
                return result
        return -1


sol = Solution()
# print(sol.search([4, 5, 6, 7, 0, 1, 2, 3], 4))
# print(sol.search([9, 10, 3, 5, 6, 8], 5))
print(sol.search([1, 7, 67, 133, 178], 1))
```
