

## THIS PROBLEM IS NOT YET SOLVED

## Minimum Difference
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/122344/homework/problems/1104?navref=cl_tt_lst_sl

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/026-minimum-difference-question.png)

### Approach

```py
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle)+1)

        for row in triangle[::-1]:
            for i, n in enumerate(row):
                dp[i] = n + min(dp[i], dp[i+1])
                print(dp)
        return dp[0]
```