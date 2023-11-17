
## Container with most water
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/120854/assignment/problems/169/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/033-container-with-most-water-question.png)

### Approach
- Two pointers

```py
class Solution:
	# @param A : list of integers
	# @return an integer
    def maxArea(self, A):
        i,j = 0,len(A)-1
        ans = 0
        while i < j:
            area = (j-i) * min(A[i],A[j])
            ans = max(ans,area)
            if A[i] < A[j]:
                i += 1
            else:
                j -= 1
        return ans

sol = Solution()
print(sol.maxArea([1, 5, 4, 3]))
print(sol.maxArea([1, 5, 6,4, 2]))
```

