

## Tower of Hanoi
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/81717/assignment/problems/15010?navref=cl_tt_lst_sl

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/019-tower-of-hanoi-question.png)

### Approach

```py
class Solution:
    # @param A : integer
    # @return a list of list of integers
    def towerOfHanoi(self, A):

        result = []
        def hanoi(rods,from_rod, to_rod, aux_rod):
            if rods == 0:
                return
            hanoi(rods-1,from_rod,aux_rod,to_rod)
            result.append([rods,from_rod,to_rod])
            hanoi(rods-1,aux_rod, to_rod, from_rod)

        hanoi(A,1,3,2)
        return result

sol = Solution()
# print(sol.towerOfHanoi(1))
# print(sol.towerOfHanoi(2))
print(sol.towerOfHanoi(3))

```