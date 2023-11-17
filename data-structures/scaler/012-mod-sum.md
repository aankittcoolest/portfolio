
## Mod sum
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/81679/homework/problems/4745/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/012-mod-sum-question.png)

### Approach
- Take mod and check frequency

```py
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        count = [0] * 1001
        for element in A:
            count[element] += 1

        ans = 0
        mod = 1000000000 + 7
        for i in range(1, 1001):
            for j in range(1, 1001):
                val = i % j
                temp = count[i] * count[j] * val
                ans = ((ans % mod) + (temp % mod)) % mod
        return ans % mod


sol = Solution()
print(sol.solve([17, 100, 11]))
print(sol.solve([1, 2, 3]))

```