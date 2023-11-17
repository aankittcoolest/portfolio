

## Factorial Array
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/81675/homework/problems/2206/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/017-factorial-array-question.png)


### Approach

```py
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        pf = self.primeFactors(A[len(A)-1])

        k = 0
        count = 0
        total_count = 0

        mod = 10 ** 9 + 7
        for factor in pf:
            for i in range(k, len(A)):
                if A[i] < 2:
                    k += 1
                elif A[i] < factor:
                    count += 1
                else:
                    break
            if count > 0:
                subsequences = pow(2, count, mod) - 1
                total_count = total_count + subsequences
                k += count
                count = 0

        total_count = total_count + pow(2, len(A[k:]), mod) - 1
        total_count = total_count % mod
        return total_count

    def primeFactors(self, num):
        prime = [True for i in range(num+1)]
        # boolean array
        p = 2
        while (p * p <= num):

            # If prime[p] is not
            # changed, then it is a prime
            if (prime[p] == True):

                # Updating all multiples of p
                for i in range(p * p, num+1, p):
                    prime[i] = False
            p += 1

        l = []
        for p in range(2, num+1):
            if prime[p]:
                l.append(p)
        return l


sol = Solution()
print(sol.solve([251, 923, 561, 230, 100, 399, 542, 198, 548, 892, 721, 781, 174, 809, 9, 232, 165, 861, 36, 837, 377, 313, 475, 269, 210, 530, 940, 570, 24, 434, 764, 275, 709, 325, 505, 161, 724, 47, 359, 625, 291, 81, 406, 465, 242, 767, 698, 408, 629,
      86, 597, 358, 399, 72, 979, 962, 603, 919, 884, 627, 353, 1, 254, 414, 678, 111, 575, 755, 511, 287, 380, 802, 720, 138, 620, 314, 905, 670, 74, 886, 756, 671, 244, 508, 744, 224, 822, 347, 495, 706, 326, 201, 707, 580, 615, 386, 43, 543, 141, 554]))
```