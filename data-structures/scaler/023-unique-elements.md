
## Unique Elements
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/81709/assignment/problems/1224/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/023-unique-elements-question.png)

### Approach

```py
class Solution:
    def solve(self, A):
        A.sort()
        count = 0
        for i in range(1,len(A)):
            if A[i-1] < A[i]:
                continue
            else:
                # if element is equal to previous element,
                # we increase the count
                count = count + (A[i-1] - A[i]) + 1
                # we increase the value of the current element
                A[i] = A[i] + (A[i-1] - A[i]) + 1
        return count
```