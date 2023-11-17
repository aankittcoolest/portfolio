
## Consecutive numbers sum
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/127963/homework/problems/6707?navref=cl_tt_lst_sl

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/039-consecutive-numbers-sum-question.png)

### Approach
- two pointers
- maths

```text
A = (x + 1) + (x+2) + (x+3) +...+ (x+k)
A = kx + (1 + 2 + 3...k)
A = kx + k(k-1)/2
A - k(k-1)/2 = kx
x = (A-k(k-1)/2)/k
```

```py
class Solution:
    def solveTwoPointers(self, A):
        i = 1
        j = 1
        sum = 0
        count = 0
        while i <= A:
            sum = sum + j
            if sum < A:
                j += 1
            else:
                while sum >= A:
                    if sum == A:
                        count += 1
                    sum = sum - i
                    i += 1
                j += 1
        return count

    def solve(self, A):
        k = 1
        count = 0
        while True:
            T = A - (k * (k-1)/2)
            if T <= 0:
                break
            if T % k == 0:
                count += 1
            k += 1
        return count


sol = Solution()
print(sol.solve(15))
print(sol.solve(5))
print(sol.solve(11084))
```