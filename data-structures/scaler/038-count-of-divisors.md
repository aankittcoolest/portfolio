
## Count of divisors
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/128059/assignment/problems/4107/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/038-count-of-divisors-question.png)

### Approach
- maths
- spf (smallest prime factors)

```py
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        mx = max(A)
        spf = [i for i in range(mx + 1)]

        def calculateSpf():
            i = 2
            while i*i <= mx:
                j = i*i
                if spf[i] == i:
                    while j <= mx:
                        if spf[j] == j:
                            spf[j] = i
                        j += i
                i += 1

        calculateSpf()
        print(spf)

        i = 0
        for num in A:
            temp = num
            ans = 1
            while temp != 1:
                pow = 1
                d = spf[temp]
                while temp != 1 and temp % d == 0:
                    pow += 1
                    temp = temp//d
                ans *= pow
            A[i] = ans
            i += 1
        return A


sol = Solution()
print(sol.solve([2, 3, 4, 5]))
```