## Find maximum sorted subarray
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/100260/assignment/problems/359?navref=cl_tt_lst_sl

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/025-maximum-unsorted-subarray-question.png)


### Approach


```py
import sys


class Solution:
    def subUnsort(self, A):

        # find a and b which are potential left and right
        i = 0
        a = -1
        b = -1
        while i < len(A)-1:
            if A[i] <= A[i+1]:
                i = i + 1
            else:
                a = i
                break

        i = len(A) - 1

        while i > 0:
            if A[i] >= A[i-1]:
                i = i - 1
            else:
                b = i
                break

        if a == -1:
            return [-1]

        # find max and min between a and b
        min = sys.maxsize
        max = -1

        for i in range(a, b+1, 1):
            if min > A[i]:
                min = A[i]
            if max < A[i]:
                max = A[i]

        # find value [0,a] which is greater than minimum of [a,b]
        for i in range(0, a+1, 1):
            if A[i] > min:
                a = i
                break

        # find value [b,n] which is less than maxiumum of [a,b]
        for i in range(len(A)-1, b-1, -1):
            if A[i] < max:
                b = i
                break

        return [a, b]


sol = Solution()
# print(sol.subUnsort([2, 3, 5, 7, 10, 6, 11, 15, 18, 20]))
# print(sol.subUnsort([2, 3, 5]))

# print(sol.subUnsort([1,1,10,10,15,10,15,10,10,15,10,15]))
print(sol.subUnsort([1,1,10,10,15,10,15,10,10,15,10,15]))
print(sol.subUnsort([3,3,4,5,5,9,11,13,14,15,15,16,15,20,16]))
```