
## Heaters
- Ref: https://leetcode.com/problems/heaters/description/

### Approach
- binary search

```py
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        def binSearchHigh(lo, hi, val):
            while lo < hi:
                mid = (lo + hi)//2
                if heaters[mid] < val:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        lo = 0
        hi = len(heaters)-1
        diff = 0
        diff1 = diff2 = 0

        for house in houses:
            ans = binSearchHigh(lo, hi, house)
            diff1 = abs(house-heaters[ans])
            if ans > 0:
                diff2 = abs(house-heaters[ans-1])
                diff = max(diff, min(diff1, diff2))
            else:
                diff = max(diff, diff1)
            if ans != lo:
                lo = ans
        return diff
```