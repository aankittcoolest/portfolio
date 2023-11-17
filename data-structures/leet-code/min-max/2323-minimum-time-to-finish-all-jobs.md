

## Minimum time to finish all jobs
- Ref: https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs-ii/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency

### Approach
- min-max

```py
from typing import List


class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        jobs.sort(reverse=True)
        workers.sort(reverse=True)
        for i, _ in enumerate(jobs):
            jobs[i] = jobs[i]//workers[i] if jobs[i]% workers[i] == 0 else jobs[i]//workers[i] + 1
        return max(jobs)


sol = Solution()
print(sol.minimumTime([5, 2, 4], [1, 7, 5]))
print(sol.minimumTime([3,18,15,9],[6,5,1,3]))
print(sol.minimumTime([1], [2]))
print(sol.minimumTime([5], [2]))
```