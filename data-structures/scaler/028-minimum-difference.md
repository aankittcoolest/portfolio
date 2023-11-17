
## Minimum difference
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/120942/homework/problems/1104/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/028-minimum-difference-question.png)


### Approach
- sorting
- binary search


```py
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of list of integers
    # @return an integer
    def solve(self, A, B, C):

        for list in C:
            list.sort()

        ans = 1000
        for i in range(0, A-1):
            for j in range(0, B):
                res = self.binarySearch(C[i+1], C[i][j])
                ans = min(ans, abs(C[i][j]-C[i+1][res[0]]),
                          abs(C[i+1][res[1]]-C[i][j]))
        return ans

    def binarySearch(self, arr, element):
        l = 0
        r = len(arr)-1
        mid = 0

        while l <= r:
            mid = (l+r) // 2
            if arr[mid] > element:
                r = mid - 1
            elif arr[mid] < element:
                l = mid + 1
            elif arr[mid] == element:
                if mid > 0:
                    return (mid-1, mid)
                else:
                    return (mid, mid+1)
        if mid+1 < len(arr):
            return (mid, mid+1)
        else:
            return (mid-1, mid)


a = [
    [9, 4, 3, 6],
    [7, 5, 2, 1],
    [1, 9, 3, 4],
    [6, 4, 5, 8],
]

sol = Solution()
sol.solve(4, 4, a)

# print(sol.binarySearch([1,2,4,5,10,15,19],12))
# print(sol.binarySearch([1, 2, 4, 5, 10, 15, 19], 20))
# print(sol.binarySearch([2, 4, 5, 10, 15, 19], 1))
```