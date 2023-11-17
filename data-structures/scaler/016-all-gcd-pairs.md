
## All GCD pairs
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/81691/homework/problems/5880


## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/016-all-gcd-pairs-question.png.png)

### Approach
- GCD
- hashmap

```py
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        A.sort()
        A.reverse()
        d = {}

        def gcd(B, C):
            if C == 0:
                return B
            return gcd(C, B % C)

        res = []
        for element in A:
            if d.get(element) is not None:
                if d[element] > 0:
                    d[element] -= 1
                else:
                    del d[element]
            else:
                for el in res:
                    x = gcd(el, element)
                    if d.get(x) is None:
                        d[x] = 2
                    else:
                        d[x] = d[x] + 2
                res.append(element)
        return res


sol = Solution()
# sol.solve([2, 2, 2, 2, 8, 2, 2, 2, 10])
print(sol.solve([46, 1, 2, 1, 1, 1, 5, 45, 1, 1, 2,
      5, 1, 40, 1, 1, 1, 1, 1, 1, 1, 1, 1, 31, 1]))
```
