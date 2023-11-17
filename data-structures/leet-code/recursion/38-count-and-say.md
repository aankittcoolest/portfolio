
## Count and say
- Ref: https://leetcode.com/problems/count-and-say/description/


### Approach
- recursion


```py
class Solution:
    def say(self, combination: str) -> str:
        count = 0
        comp = ""
        res = ""

        for s in combination:
            if comp == "":
                comp = s
                count = 1
                continue

            if comp == s:
                count += 1
            else:
                res = res + str(count) + comp
                comp = s
                count = 1

        res = res + str(count) + comp
        return res

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        return self.say(self.countAndSay(n-1))


sol = Solution()
# sol.say("3322251")
# print(sol.say("21"))
print(sol.countAndSay(5))
```
