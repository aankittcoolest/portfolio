
## Allocate books
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/120818/homework/problems/270/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/030-allocate-books-question.png)


### Approach
- Binary search

```py
class Solution:
    def books(self, A, B):

        # when there are more students
        # then number of books allocation is not possible
        if len(A) < B:
            return -1

        # when all books is assigned to same student
        worst_case = sum(A)

        # best case = max of current array
        best_case = max(A)

        left = best_case
        right = worst_case

        # binary search
        while left <= right:
            mid = (left + right)//2

            total = 0
            students = 1
            for pages in A:
                total += pages
                if total > mid:
                    total = pages
                    students = students + 1

            if students <= B:
                right = mid - 1
            else:
                left = mid + 1

        return left


sol = Solution()
print(sol.books([12, 34, 67, 90], 2))
print(sol.books([73,58,30,72,44,78,23,9],5))
```
