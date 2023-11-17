
## Pairs with given difference
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/120854/assignment/problems/9323/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/033-pairs-with-given-difference-question.png)


### Approach
- hashmap

```py
import collections
class Solution:
    def solve(self, A, B):
        count = collections.defaultdict(int)
        res = 0
        for element in A:
            count[element] += 1
        for key in count.keys():
            second_key = key-B
            if second_key == key and count[key] > 1:
                res += 1
            elif second_key != key and count.get(second_key) is not None:
                res += 1
        return res


sol = Solution()
# print(sol.solve([1, 5, 3, 4, 2],3))
print(sol.solve([1, 1, 1, 2, 2],0))
# print(sol.solve([8, 12, 16, 4, 0, 20],4))
print(sol.solve([1,2],0))
```