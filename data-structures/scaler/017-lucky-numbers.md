
I think that the solution of this problem using binary search is wrong.
I am just trying to understand how the current editor python solution

## Lucky numbers
- Find numbers with maximum of two prime divisors
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/128059/homework/problems/1095/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/017-lucky-numbers-question.png)

### Approach

```py
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        dict = {}
        for i in range(1,A+1):
            dict[i] = {"isPrime": True, "primeFactors": [] }
        for i in range(2,A+1,1):
            j=i
            while j <= A:
                if j == i:
                    j = j + i
                    continue
                if j%i == 0 and dict[i]["isPrime"]:
                    dict[j]["primeFactors"].append(i)
                    dict[j]["isPrime"] = False
                j = j + i

        count = 0
        for key in dict.keys():
            if len(dict[key]["primeFactors"]) == 2:
                count += 1
        return count

sol = Solution()
print(sol.solve(8))
print(sol.solve(12))

```


```py
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        d = {}

        i = 2
        while i <= A:
            j = i
            if d.get(j):
                i+=1
                continue
            while j <= A:
                if d.get(j):
                    d[j] += 1
                else:
                    d[j] = 1
                j += i
            i += 1

        ans = 0
        for val in d.values():
            if val == 2:
                ans += 1

        return ans


sol = Solution()
print(sol.solve(10))
print(sol.solve(12))
```