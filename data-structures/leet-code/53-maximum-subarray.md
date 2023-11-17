
## Maximum subarray
- Ref: https://leetcode.com/problems/maximum-subarray/description/

### Approach
- kadane's algorithm

```py
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        maxSum = 0
        
        for n in nums:
            sum += n
            if sum > maxSum:
                maxSum = sum
            if sum < 0:
                sum = 0

        if maxSum == 0:
            return max(nums)

        return maxSum
```

```py
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize our variables using the first element.
        current_subarray = max_subarray = nums[0]
        
        # Start with the 2nd element since we already used the first one.
        for num in nums[1:]:
            # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)
        
        return max_subarray
```