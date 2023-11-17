
## Number of open doors
Ref: https://www.scaler.com/academy/mentee-dashboard/class/81675/assignment/problems/4106

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/017-number-of-open-doors-question.png)

### Approach:

```py
## Number of open doors


class Solution:
    ## Approach1: Find all divisors from 1-> A and 
    ## calculate numbers who have odd number of factors
    def solveBrute(self, A):
        dict = {}
        for i in range(1,A+1,1):
                dict[i] = []

        for key in dict.keys():
            for j in range(key,A+1,key):
                dict[j].append(key)

        num_open_doors = 0
        for key in dict.keys():
            if len(dict[key]) %2 !=0:
                num_open_doors += 1

        return num_open_doors

    ## Approach1: Since factors come in pairs, we just need to find
    ## numbers which form perfect square.
    ## Total number of perfect squares = sqrt(A)
    ## We can use binary search to calculate the square root of A
    ## Time complexity of solution = O(logA)
    def solve(solve, A):
        def binarySearch(A):
            start = 1
            end = A
            mid = (end+start) //2
            while start <= mid:
                if mid * mid > A:
                    # we move to left
                    end = mid-1
                elif mid * mid <= A:
                    # we move to right
                    start = mid+1
                mid = (end+start) //2
            return mid

        return binarySearch(A)



sol = Solution()
# sol.solve(10)
print(sol.solve(5))
print(sol.solve(40))
print(sol.solve(100))
```