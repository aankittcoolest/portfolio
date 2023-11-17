

## Generate all parenthesis
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/81717/assignment/problems/139/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/019-generate-all-parenthesis-question.png)


### Approach
```py
class Solution:
    def generateParenthesis(self, A):

        out = []
        def findParens(n,start,end, str):
            if start > n or end > n:
                return
            if start == end == n:
                out.append(str)
            findParens(n,start+1,end,str=str+"(")
            if end < start:
                findParens(n,start,end+1,str=str+")")
        
        findParens(A,0,0,"")
        return out
```