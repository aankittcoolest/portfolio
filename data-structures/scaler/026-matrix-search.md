
## Matrix search
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/122344/homework/problems/196

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/026-matrix-search-question.png)

```py
class Solution:

    def oneDimBinarySearch(self, A, B):
        start = 0
        end = len(A)-1
        while start <= end:
            mid = (start + end) //2
            if B == A[mid]:
                return [mid,mid]
            if B < A[mid]:
                end = mid-1
            if B > A[mid]:
                start = mid + 1

        return [start,end]

    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        C = []
        for items in A:
            C.append(items[len(items)-1])


        valid_items = self.oneDimBinarySearch(C,B)

        #it would mean that the index is found
        if valid_items[0] == valid_items[1]:
            return 1
        
        if valid_items[0] > len(A)-1:
            return 0

        valid_items = self.oneDimBinarySearch(A[valid_items[0]],B)

        #it would mean that the index is found
        if valid_items[0] == valid_items[1]:
            return 1

        # Else item should not be found
        return 0



sol = Solution()
# print(sol.oneDimBinarySearch([7,10,20,30,50],10))
# print(sol.oneDimBinarySearch([7,10,20,30,50],25))
# print(sol.oneDimBinarySearch([7,10,30,50],25))
# print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],3))
# print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],4))
# print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],11))
# print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],7))
# print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],20))
# print(sol.searchMatrix([ [3], [29], [36], [63], [67], [72], [74], [78], [85] ],41))

print(sol.searchMatrix( [[22, 32, 67]], 93))
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],50))
```
