
## Permutations of A and B
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/121054/assignment/problems/1089/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/036-permutations-of-A-and-B-question.png)


### Approach
- hashmap

```py
class Solution:
    def solve(self, A, B):
        d1 = {}
        for c in A:
            if d1.get(c):
                d1[c] += 1
            else:
                d1[c] = 1

        window = B[:len(A)]
        ans = 0

        d2 = {}
        for c in window:
            if d2.get(c):
                d2[c] += 1
            else:
                d2[c] = 1


        def compare(hm1, hm2):
            for key in hm1.keys():
                if hm2.get(key) and hm1[key] == hm2[key]:
                    continue
                else:
                    return False
            return True

        ans = 0
        if compare(d1, d2):
            ans += 1

        i = 0
        for j in range(len(window), len(B)):
            d2[B[i]] = d2[B[i]]-1
            i += 1
            if d2.get(B[j]):
                d2[B[j]] += 1
            else:
                d2[B[j]] = 1
            if compare(d1, d2):
                ans += 1

        return ans


sol = Solution()
print(sol.solve("abc", "abcbacabc"))
print(sol.solve("aca", "acaa"))
print(sol.solve("p", "pccdpeeooadeocdoacddapacaecb"))
```