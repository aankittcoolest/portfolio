
## Longest subsequence without repeat
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/121010/homework/problems/161/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/037-longest-subsequence-without-repeat-question.png)

### Approach
- two pointers

```py
class Solution:
    def lengthOfLongestSubstring(self, A):
        i = 0
        j = 0
        d = {}
        ln = 0
        while j < len(A):
            if d.get(A[j]) is None:
                d[A[j]] = True
                j += 1
            else:
                ln = max(ln, j-i)
                while d.get(A[j]):
                    del d[A[i]]
                    i += 1
                d[A[j]] = True
                j += 1
        ln = max(ln, j-i)
        return ln
```