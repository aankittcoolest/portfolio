

## Rabin carp
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/121054/assignment/problems/37597/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/036-rabin-carp-question.png)


### Approach
- rabin carp
- convert string to digit
- prevent hash collisions

```py
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        m = len(B)
        prime = 31

        p_pow = [0] * m
        p_pow[0] = 1

        mod = 10 ** 9 + 7

        for i in range(1, m):
            p_pow[i] = (p_pow[i-1] * prime) % mod

        hashB = 0
        for i in range(0, m):
            hashB += ((ord(B[i]) - ord('a')+1) * p_pow[m-i-1]) % mod

        hashA = 0
        for i in range(0, m):
            hashA += ((ord(A[i]) - ord('a')+1) * p_pow[m-i-1]) % mod

        ans = 0
        if hashA == hashB:
            ans += 1

        k = 0
        for i in range(m, n):
            hashA = hashA - ((ord(A[k]) - ord('a')+1) * p_pow[m-1])
            hashA = (hashA * prime) % mod
            hashA = (hashA + (ord(A[i]) - ord('a')+1)) % mod
            k += 1

            if hashA == hashB:
                ans += 1
        return ans


sol = Solution()
print(sol.solve("acbac", "ac"))
print(sol.solve("aaaa", "aa"))
print(sol.solve("ccbcdaacc", "ac"))
```
