
## Pair with given sum
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/120854/assignment/problems/5097/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/033-pair-with-given-sum-question.png)

### Approach
- Two pointers

```py
class Solution:
    def solve(self, A, B):
        i, j = 0, len(A)-1

        count = 0
        mod = 1000000000 + 7
        while i < j:
            sum = A[i] + A[j]
            if sum > B:
                j -= 1
            elif sum == B:
                if A[i] == A[j]:
                    x = j-i+1
                    count = ((count % mod) + (((x*(x-1))//2) % mod))
                    break
                else:
                    a = 0
                    k = i
                    while A[i] == A[k]:
                        a += 1
                        k += 1
                    i = i + a

                    b = 0
                    k = j
                    while A[j] == A[k]:
                        b += 1
                        k -= 1
                    j = j - b
                    count = ((count % mod) + ((a * b) % mod)) % mod
            else:
                i += 1
        return count % mod


sol = Solution()
# print(sol.solve([1, 5, 7, 7, 10], 8))
print(sol.solve([1, 1, 1, 1], 2))
print(sol.solve([1, 1, 1], 2))
# print(sol.solve([2, 3, 5, 6, 10], 6))
# print(sol.solve([1, 2, 6, 6, 7, 9, 9], 13))
print(sol.solve([2,3,3,5,7,7,8,9,9,10,10],11))
```