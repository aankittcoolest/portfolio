
## Matrix median
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/122354/homework/problems/357/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/027-matrix-median-question.png)


### Approach


```py
class Solution:
    def findMedian(self, A):
        m = len(A)
        n = len(A[0])

        accept_answer = ((m * n)//2) + 1

        low = 0
        high = 0
        for row in A:
            high = max(max(row),high)

        ans = -1
        while low <= high:
            mid = (low + high)//2
            # mid = low + (high-low)//2
            count = 0
            for row in A:
                count += self.getCount(row, mid)
            # move left
            if count >= accept_answer:
                ans = mid
                high = mid - 1
            # move right
            if count < accept_answer:
                low = mid + 1
        return ans

    # function to get count of elements less than or equal to B
    def getCount(self, A, B):
        low = 0
        high = len(A)-1
        mid = (low + high)//2

        ans = -1
        while low <= high:
            mid = (low + high)//2
            if A[mid] <= B:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1
        if ans == -1:
            return len(A)
        return ans
```