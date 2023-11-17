
## Divisor game
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/81691/homework/problems/2126/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/016-divisor-game-question.png)

### Approach
```py
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        lcm = (B * C)/self.gcd(B,C)
        return int(A/lcm)


    def gcd(self,A,B):
        if B==0:
            return A
        return self.gcd(B,A%B)


sol = Solution()
print(sol.solve(12, 3, 2))
print(sol.solve(4, 1, 4))
print(sol.solve(411753753,1876, 7430)) #59
print(sol.solve(81991, 2549, 7))
```