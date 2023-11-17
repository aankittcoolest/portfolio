
## Prime sum
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/128059/homework/problems/297/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/038-prime-sum-question.png)

### Approach
- sieve of eranthoses

```py
class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        soe = [True] * (A+1)
        for i in range(2, A+1):
            for j in range(i*i, A+1, i):
                soe[j] = False

        for i in range(2,len(soe)+1):
            if soe[i] == soe[A-i] == True:
                return [i, A-i]
```