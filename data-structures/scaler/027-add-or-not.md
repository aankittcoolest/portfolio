
## Add or Not
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/122354/homework/problems/5153/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/027-add-or-not-question.png)

### Approach

```py
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        A.sort()
        print(A)
        pf = [0] * (len(A) + 1)

        for i in range(0,len(A)):
            pf[i+1] = A[i] + pf[i]
        print(pf)

        max = -1
        element = None
        for i,item in enumerate(A):
            low = 1
            high = i+1
            if i == 6:
                while low <= high:
                    mid = (low + high)//2
                    print(mid)
                    bounds = (item * mid) - (pf[i+1] - pf[i+1-mid])
                    if bounds <= B:
                        if mid > max:
                            max = mid
                            element = item
                        low = mid + 1
                    else:
                        high = mid - 1

        return [max,element]


sol = Solution()
# print(sol.solve([3,1,2,2,1],3))
# print(sol.solve([5,5,5],3))
print(sol.solve([-5,6,1,-5,1,-3,1,3,1,5],9))
```