
## Shaggy and distances
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/120870/assignment/problems/1302/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/032-shaggy-and-distances-question.png)

### Approach
- hashmap

```py
class Solution:
    def solve(self, A):
        d = {}

        for element in A:
            d[element] = -1

        ans = float("inf")
        for i,element in enumerate(A):
            if d.get(element) == -1:
                d[element] = i
            else:
                ans = min(ans,i-d.get(element))
                d[element] = i
        if ans == float("inf"):
            return -1
        return ans

sol = Solution()
print(sol.solve([7, 1, 3, 4, 1, 7]))
```