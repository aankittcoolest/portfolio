
## Enumerating GCD
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/81691/homework/problems/967/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/016-enumerating-gcd-question.png)


### Approach
- gcd

```py
class Solution:
    def solve(self, A, B):
        if A == B:
            return A
        return 1
```