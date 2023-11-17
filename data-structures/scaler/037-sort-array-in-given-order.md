
## Sort array in given order
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/121010/homework/problems/4808/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/037-sort-array-in-given-order-question.png)

### Approach
- hashmap

```py
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        d = {}
        for element in A:
            if d.get(element):
                d[element] += 1
            else:
                d[element] = 1

        ans = []
        for element in B:
            if d.get(element):
                while d.get(element) > 0:
                    ans.append(element)
                    d[element] -= 1
                del d[element]
        B = [*d]
        B.sort()
        for element in B:
            while d.get(element) > 0:
                ans.append(element)
                d[element] -= 1
            del d[element]

        return ans


sol = Solution()
print(sol.solve([1, 2, 3, 4, 5, 4], [5, 4, 2]))
print(sol.solve([5, 17, 100, 11], [1, 100]))
print(sol.solve([15,5,10,6,14], [8,16,6,2,13,1,12,3,14]))
print(sol.solve([3,20,17,17], [5,9,20,11,6,18,7,13]))
```
