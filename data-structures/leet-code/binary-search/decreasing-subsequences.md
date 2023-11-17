
## Decreasing subsequences
- Ref: https://leetcode.com/discuss/interview-question/350233/Google-or-Summer-Intern-OA-2019-or-Decreasing-Subsequences

### Approach
- binary search

```py
class Solution:

    def decreasingSubsequences(self, nums):
        piles = [0] * len(nums)
        size = 0

        def binSearch(nums, lo, high, val):
            while lo < high:
                mid = (lo+high)//2
                if nums[mid] <= val:
                    lo = mid + 1
                else:
                    high = mid
            return lo

        for num in nums:
            pile = binSearch(nums, 0, size, num)
            piles[pile] = num
            if pile == size:
                size += 1
        return size


sol = Solution()
sol.decreasingSubsequences([2, 9, 12, 13, 4, 7, 6, 5, 10])
```
