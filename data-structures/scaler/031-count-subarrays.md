
## Count subarrays
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/121022/homework/problems/1226/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/031-count-subarrays-question.png)


### Approach
- Two pointers
- Hashmap

```py
class Solution:
    def solve(self, A):
        d = {}
        l = 0
        r = 0
        ans = 0
        for element in A:
            if d.get(element) is not None:
                while A[l] != element:
                    del d[A[l]]
                    l += 1
                del d[A[l]]
                l += 1

            d[element] = 1
            r += 1
            ans += r-l
        return ans % 1000000007


sol = Solution()
sol.solve([2, 3, 2, 5, 2, 3])
sol.solve([2, 3, 4, 3, 2, 3])  # Exp: 13

```