
## Longest consecutive sequence
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/120870/assignment/problems/152/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/032-longest-consecutive-sequence-question.png)


### Approach
- hashmap

```py
from collections import Counter
class Solution:
	# @param A : tuple of integers
	# @return an integer
    def longestConsecutive(self, A):
        counter = Counter(A)

        ans = 0
        for element in A:
            if counter.get(element-1) is not None:
                continue
            else:
                count = 0
                while counter.get(element):
                    element = element + 1
                    count += 1 
                ans = max(ans,count)
        return ans

sol = Solution()
print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))
```
