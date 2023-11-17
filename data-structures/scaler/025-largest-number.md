

## Build largest number from array
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/100260/homework/problems/64

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/025-largest-number-question.png)

### Approach

```py
from functools import cmp_to_key


class Solution:

    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        def comparision(a, b):
            first = str(a)
            second = str(b)
            if first + second < second + first:
                return 1
            elif first + second > second + first:
                return -1
            return 0

        B = sorted(A, key=cmp_to_key(comparision))
        out = ""
        for i in B:
            out += str(i)
        
        start_idx=-1
        for i in out:
            start_idx += 1
            if i == "0":
                continue
            break

        return out[start_idx:]


sol = Solution()
# sol.countSort([1,2,9,2,1,9])

print(sol.largestNumber([100, 101, 11, 10, 9]))
print(sol.largestNumber([100,101,11,10,9, 2]))
print(sol.largestNumber([0,0,0,0]))
print(sol.largestNumber([0,8,0,0]))
# print(sol.largestNumber([2, 3, 9, 0]))
```
