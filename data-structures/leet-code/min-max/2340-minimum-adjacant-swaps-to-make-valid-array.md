
## Minimum adjacant swaps to make valid array
- Ref: https://leetcode.com/problems/minimum-adjacent-swaps-to-make-a-valid-array/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency

### Approach
- min-max

```py
class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        mn = 10 ** 5 + 1
        mx = -1
        minIndex = 0
        maxIndex = 0
        # find min and it's index
        for i, num in enumerate(nums):
            if num < mn:
                mn = num
                minIndex = i

        # find max and it's index
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > mx:
                mx = nums[i]
                maxIndex = i

        if maxIndex >= minIndex:
            return minIndex + len(nums)-1-maxIndex
        else:
            return minIndex + (len(nums)-1-maxIndex) - 1
```