
## Find peak element using binary search
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/122344/assignment/problems/4132

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/026-peak-element-using-binary-search-question.png)


```py
# class Solution:
#     # @param A : list of integers
#     # @return an integer
#     def solve(self, A):
#         def binarySearch(start, end):
#             if start == end:
#                 return A[start]

#             mid = (start + end)//2
#             peak1 = binarySearch(start, mid)
#             peak2 = binarySearch(mid+1, end)

#             if peak1 > peak2:
#                 return peak1
#             return peak2

#         start = 0
#         end = len(A) -1

#         return binarySearch(start, end)


# sol = Solution()
# print(sol.solve([1,2,3,4,5]))
# print(sol.solve([5,17,100,11]))


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        nums = A
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return nums[l]


sol = Solution()
print(sol.solve([10,18,11,12,13,14,15,16]))
```