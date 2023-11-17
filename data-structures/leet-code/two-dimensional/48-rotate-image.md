

## Rotate image
- Ref: https://leetcode.com/problems/rotate-image/description/?envType=study-plan-v2&envId=top-interview-150

### Approach
- transpose
- reflection of matrix

```py
from typing import List


class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        n = len(m)-1
        mm = len(m)//2
        k = 0
        for i in range(mm):
            for j in range(i, n-i):
                m[i][j], m[n-i-j+k][i] = m[n-i-j+k][i], m[i][j]
                m[n-i-j+k][i], m[n-i][n-j] = m[n-i][n-j], m[n-i-j+k][i]
                m[n-i][n-j], m[j][n-i] = m[j][n-i], m[n-i][n-j]
            k +=1


sol = Solution()
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sol.rotate(m)
print(m)

m = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
sol.rotate(m)
print(m)
```

```py
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reflect(matrix)
    
    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]
```