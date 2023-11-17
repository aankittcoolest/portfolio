
## Find all primes
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/128059/assignment/problems/35398/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/038-find-all-primes-question.png)

### Approach
- Sieve of Eranthoses

```py
class Solution:
    # @param A : integer
    # @return a list of integers
    def solve(self, A):
        soe = [True] * (A+1)
        soe[0] = soe[1] = False

        i = 2
        while i <= A:
            j = i*i
            while j <= A:
                soe[j] = False
                j += i
            i += 1

        result = []
        for i, element in enumerate(soe):
            if element:
                result.append(i)

        return result


sol = Solution()
print(sol.solve(10))
```
