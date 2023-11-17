

## Boring substring
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/121054/assignment/problems/5550/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/036-boring-substring-question.png)

### Approach
- Convert string to digits

```py
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        even = []
        odd = []
        for element in A:
            if (ord(element)-ord("a")) % 2 == 0:
                even.append(element)
            else:
                odd.append(element)

        even.sort()
        odd.sort()

        if len(odd) == 0 or len(even) == 0:
            return 1

        if abs(ord(odd[len(odd)-1])-ord(even[0])) != 1:
            return 1
        if abs(ord(even[len(even)-1]) - ord(odd[0])) != 1:
            return 1
        return 0


sol = Solution()
# print(sol.solve("abcd"))
# print(sol.solve("abc"))
print(sol.solve('nmnn'))
```
