## Candy
- Ref: https://leetcode.com/problems/candy/description/?envType=study-plan-v2&envId=top-interview-150

## Approach
- Two pass problem

```py
class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i-1] < ratings[i]:
                candies[i] = candies[i-1] + 1

        for i in range(len(candies)-2, -1, -1):
            if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
                candies[i] = candies[i+1] + 1

        return sum(candies)


sol = Solution()
print(sol.candy([1, 4, 3, 2, 4, 2]))
print(sol.candy([1, 0, 2]))
print(sol.candy([1, 3, 4, 5, 2]))

```