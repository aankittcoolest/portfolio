

## Sub matrix sum
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/81685/assignment/problems/4088/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/009-sub-matrix-sum-question.png)


### Approach

```py
class Solution:
    def solve(self, A, B, C, D, E):
        mod = 1000000007
        for i,l in enumerate(A):
            for j in range(1,len(l)):
                A[i][j] = ((A[i][j-1] % mod) + (A[i][j] % mod)) % mod

        for i,l in enumerate(A):
            if i == 0:
                continue
            for j in range(0,len(l)):
                A[i][j] = ((A[i-1][j] % mod) + (A[i][j] % mod)) % mod


        for i,_ in enumerate(B):
            B[i] = B[i]-1
            C[i] = C[i]-1
            D[i] = D[i]-1
            E[i] = E[i]-1

        F = []
        for i,_ in enumerate(B):
            if B[i] == 0 and C[i] == 0:
                F.append(A[D[i]][E[i]])
            elif B[i] == 0 and C[i] > 0:
                sum = (A[D[i]][E[i]] - A[D[i]][C[i]-1] + mod)%mod
                F.append(sum)
            elif B[i] > 0 and C[i] == 0:
                sum = (A[D[i]][E[i]] - A[B[i]-1][E[i]]+mod)%mod
                F.append(sum)
            else:
                sum = (A[D[i]][E[i]] - A[D[i]][C[i]-1] + mod) % mod
                sum = (sum - A[B[i]-1][E[i]]+mod) % mod
                F.append(((sum%mod) + (A[B[i]-1][C[i]-1]%mod))%mod)
        return F



A = [   [1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]   ]
B = [1, 2]
C = [1, 2]
D = [2, 3]
E = [2, 3]

sol = Solution()
print(sol.solve(A,B,C,D,E))

A = [   [5, 17, 100, 11],
        [0, 0,  2,   8]    ]
B = [1, 1]
C = [1, 4]
D = [2, 2]
E = [2, 4]

print(sol.solve(A,B,C,D,E))
```