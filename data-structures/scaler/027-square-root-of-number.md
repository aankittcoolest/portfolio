## Square root of number
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/122354/assignment/problems/200/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/027-square-root-of-number-question.png)

### Approach

```py
class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        def binarySearch(A):
            start=0
            end=A
            mid=0
            while start<=end:
                mid = (start + end)//2
                if mid * mid == A:
                    return mid
                if mid * mid > A:
                    #shift left
                    end = mid-1
                else:
                    #shift right
                    start = mid+1

            if mid * mid > A:
                return mid-1
            return mid
        
        return binarySearch(A)


sol = Solution()
print(sol.sqrt(25))
```