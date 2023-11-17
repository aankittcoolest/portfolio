from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # we sort the list based on each interval finish time
        intervals.sort(key=lambda x: x[1])

        i = 0

        # store number of overalpping intervals
        count = 0
        for j in range(1, len(intervals), 1):
            # compare next interval start time should be greater than or equal to previous interval finish time to prove non-overlapping
            if intervals[j][0] >= intervals[i][1]:
                # print(intervals[i])
                i = j
            else:
                count += 1

        # if i has reached the end, we can safely include all the remaining intervals because they will be non-overlapping
        # if i < len(intervals):
            # print(intervals[i])

        return count


sol = Solution()
print(sol.eraseOverlapIntervals(
    [[1, 2], [2, 3], [3, 4], [1, 3], [5, 10], [10, 15]]))

