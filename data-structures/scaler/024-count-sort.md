## Count Sort
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/120695/assignment/problems/21391?navref=cl_tt_lst_sl

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/024-count-sort-question.png)


### Approach

```py
class Solution:
    def solve(self, A):
        m = max(A)
        B = [0] * (m+1)

        # frequency array
        for i in A:
            B[i] +=1

        # cumulative frequency
        for i in range(1,len(B)):
            B[i] += B[i-1]

        C = [0] * len(A)
        for i in range(len(A)-1,-1,-1):
            C[B[A[i]]-1] = A[i]
            B[A[i]] = B[A[i]]-1
        return C


sol = Solution()
print(sol.solve([1, 3, 1]))
print(sol.solve([4, 2, 1, 3]))
```