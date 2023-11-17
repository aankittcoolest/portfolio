

## Minimum swaps
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/81685/homework/problems/4048?navref=cl_tt_nv

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/009-swap-02-question.png)

### Approach

```py
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        count = 0
        for i,_ in enumerate(A):
            while i != A[i]:
                temp = A[i]
                A[i] = A[temp]
                A[temp] = temp
                count += 1
        return count
```