
## Count rectangles
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/121010/homework/problems/4759/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/037-count-rectangles-question.png)

### Approach
- hashmap


```py
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        d = {}

        for i in range(len(A)):
            if d.get((A[i], B[i])):
                d[(A[i], B[i])] += 1
            else:
                d[(A[i], B[i])] = 1

        count = 0
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                x1 = A[i]
                y1 = B[i]
                x2 = A[j]
                y2 = B[j]

                if x1 != x2 and y1 != y2:
                    if d.get((x1, y2)) and d.get((x2, y1)):
                        count += 1
        return count // 2


sol = Solution()
print(sol.solve([1, 1, 2, 2], [1, 2, 1, 2]))
print(sol.solve([1, 1, 2, 2, 3, 3], [1, 2, 1, 2, 1, 2]))
```