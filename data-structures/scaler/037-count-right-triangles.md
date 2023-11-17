
## Count right triangles
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/121010/assignment/problems/4719/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/037-count-right-triangles-question.png)


### Approach
- hashmap

```py
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        xhm = {}
        yhm = {}

        for i in range(len(A)):
            if xhm.get(A[i]):
                xhm[A[i]]+=1
            else:
                xhm[A[i]]=1

            if yhm.get(B[i]):
                yhm[B[i]]+=1
            else:
                yhm[B[i]]=1
            
        ans = 0
        for i in range(len(A)):
            ans += (xhm[A[i]]-1) * (yhm[B[i]]-1)
        
        return ans

sol = Solution()
print(sol.solve([1, 1, 2],[1, 2, 1]))
print(sol.solve([1, 1, 2, 3, 3],[1, 2, 1, 2, 1]))
```