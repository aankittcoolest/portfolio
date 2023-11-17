

## Max chunks to make array sorted
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/81709/homework/problems/4036/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/023-max-chunks-to-make-array-sorted-question.png)

### Approach

```py
class Solution:
    def solve(self, A):
        max = A[0]
        count = 0
        for i in range(0,len(A)):
            if A[i]> max:
                max = A[i]
            if i == max:
                count +=1
        return count
```