

## Maximum unsorted subarray
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/120695/homework/problems/359/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/024-maximum-unsorted-subarray-question.png)

### Approach

```py
class Solution:
    def subUnsort(self, A):
        leftBound = -1
        for i in range(0,len(A)-1,1):
            if A[i] <= A[i+1]:
                continue
            else:
                leftBound = i
                break

        if leftBound == -1:
            return [-1]

        rightBound = -1
        for i in range(len(A)-1,0,-1):
            if A[i] >= A[i-1]:
                continue
            else:
                rightBound = i
                break

        minimum = min(A[leftBound:rightBound+1])
        maximum = max(A[leftBound:rightBound+1])

        for i in range(0,leftBound+1):
            if A[i] <= minimum:
                continue
            leftBound = i
            break

        for i in range(len(A)-1,rightBound-1,-1):
            if A[i] >= maximum:
                continue
            rightBound = i
            break

        return [leftBound,rightBound]


sol = Solution()
# print(sol.subUnsort([1, 3, 2, 4, 5]))
# print(sol.subUnsort([1,1]))
# print(sol.subUnsort([1,2,3]))
# print(sol.subUnsort([1,1,10,10,15,10,15,10,10,15,10,15]))
print(sol.subUnsort([4,15,4,4,15,18,20]))
print(sol.subUnsort([1,1,2,3,3,4,8,9,11,9,11,12,12,11,9,14,19,20,20])) #[8,14]
```