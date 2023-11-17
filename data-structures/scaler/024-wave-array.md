
## Wave Array
- https://www.scaler.com/academy/mentee-dashboard/class/120695/homework/problems/267

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/024-wave-array-question.png)


### Approach

```py
class Solution:
    def wave(self, A):
        A.sort()
        for i in range(0,len(A)-1,2):
            temp = A[i+1]
            A[i+1] = A[i]
            A[i] = temp
        return A
        

sol = Solution()
sol.wave([2,1,3])
sol.wave([2,1,4,3])
```