



## Eucledian Distance
- Calculate minimum euclidian distance for B points.
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/100260/assignment/problems/4194

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/025-closest-point-to-origin-question.png)
- TODO: Understand heaps and try to solve the problem using heap.


### Approach
- Here we solve the problem using dictionary

```py
class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return a list of list of integers
    def solve(self, A, B):
        dict = {}
        for item in A:
            value = item[0] * item[0] + item[1] * item[1]
            if value not in dict.keys():
                items = []
                items.append(item)
                dict[value] = items
            else:
                dict[value].append(item)

        print(dict)
        keys = dict.keys()
        keys = sorted(keys)

        list = []
        for key in keys:
            while len(dict[key]) > 0:
                values = dict[key]
                list.append(values[0])
                dict[key] = dict[key][1:]
                print(dict)
                B = B - 1
                if B == 0:
                    return list

        return list


sol = Solution()
print(sol.solve([[1, 3], [-2, 2], [3, 1]], 4))
```