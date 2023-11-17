
## Max continuous series of ones
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/120854/homework/problems/273/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/033-max-continuous-ones-question.png)


### Approach
- two pointers
- sliding window

```py
class Solution:
    def maxone(self, A, B):
        i = 0
        index0, index1 = -1, -1
        size, maxSize = 0, 0
        temp = B

        for j, element in enumerate(A):
            if element == 1:
                size += 1
            elif element == 0 and temp > 0:
                size += 1
                temp -= 1
            elif element == 0 and temp == 0:
                while A[i] == 1:
                    size -= 1
                    i += 1
                # remove zero also from window
                # but do not reduce the size
                i += 1

            if size > maxSize:
                index0 = i
                index1 = j
                maxSize = size

        res = []
        for i in range(index0,index1+1):
            res.append(i)
        return res


sol = Solution()
print(sol.maxone([1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1], 1))
# sol.maxone([0, 0, 0, 0], 3)
```