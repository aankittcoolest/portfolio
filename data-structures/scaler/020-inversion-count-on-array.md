## Inversion count on array
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/81707/assignment/problems/4190?navref=cl_tt_lst_sl

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/020-inversion-count-on-array-question.png)

### Approach

```py
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        count = 0
        count = self.mergeSort(A, count)
        return count % 1000000007

    def mergeSort(self, A, count):
        if len(A) > 1:
            mid = len(A)//2

            la = A[:mid]
            ra = A[mid:]
            count = self.mergeSort(la, count) + self.mergeSort(ra, count)

            i = j = k = 0

            while i < len(la) and j < len(ra):
                if la[i] <= ra[j]:
                    A[k] = la[i]
                    i += 1
                else:
                    count += len(la)-i
                    A[k] = ra[j]
                    j += 1
                k += 1

            while i < len(la):
                A[k] = la[i]
                i += 1
                k += 1
            while j < len(ra):
                A[k] = ra[j]
                j += 1
                k += 1

        return count


sol = Solution()
# print(sol.solve([3, 4, 1, 2]))
print(sol.solve([4, 5, 1, 2, 7, 3]))
# print(sol.mergeSort([4, 5, 1, 2, 7, 3]))
```