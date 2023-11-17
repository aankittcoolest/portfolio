
## Kth smallest element
- Ref:  https://www.scaler.com/academy/mentee-dashboard/class/81707/assignment/problems/260/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/020-kth-smallest-element-question.png)

### Approach

```py
class Solution:
    def kthsmallest(self, A, B):
        swaps = B
        for i in range(len(A)-1,-1,-1):
            min = 10 ** 9 + 7
            index = -1
            for j in range(0,i+1):
                if A[j] < min:
                    min = A[j]
                    index = j
            A[i],A[index] = A[index],A[i]
            swaps = swaps - 1
            if swaps == 0:
                return A[len(A) - B]

sol = Solution()
print(sol.kthsmallest([2, 1, 4, 3, 2],3))
print(sol.kthsmallest([8,16,80,55,32,8,38,40,65,18,15,45,50,38,54,52,23,74,81,42,28,16,66,35,91,36,44,9,85,58,59,49,75,20,87,60,17,11,39,62,20,17,46,26,81,92], 9))

    


```