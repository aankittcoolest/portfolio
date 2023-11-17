
## Excel column title
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/127963/assignment/problems/76/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/039-excel-column-title-question.png)

### Approach
- maths

```py
class Solution:
    def convertToTitle(self, A):
        tot_chars = 26
        out = ""
        while A > 0:
            A = A-1
            temp = A % tot_chars
            out = chr(ord("A")+temp) + out
            A = A//tot_chars
        return out


sol = Solution()
print(sol.convertToTitle(300))
print(sol.convertToTitle(943566)) #BAQTZ
```