

## Combinations
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/81717/homework/problems/142/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/019-combinations-question.png)

### Approach
```py
class Solution:
    def combine(self, A, B):
        def comb(output,temp,index,N,i,K):
            if index == K > 0:
                output.append(temp.copy())
                return
            if i >= N:
                return

            temp[index] = i+1
            comb(output,temp,index+1,N,i+1,K)
            comb(output,temp,index,N,i+1,K)

        output = []
        temp = [0]*B

        comb(output,temp,0,A,0,B)
        return output


sol = Solution()
print(sol.combine(3, 2))
print(sol.combine(4, 2))
```
