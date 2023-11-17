class Solution:
    def searchRange(self,A,B):

        def leftMost(l, r):
            if l == r:
                return l
            
            mid = (l+r)//2

            if A[mid] < B:
                return leftMost(mid+1,r)
            else:
                return leftMost(l,mid)

        def rightMost(l,r):
            if l == r:
                return l
            
            mid = (l+r+1)//2

            if A[mid] > B:
                return rightMost(l,mid-1)
            else:
                return rightMost(mid,r)
        l = 0
        r = len(A)-1
        ans1 = leftMost(l,r)
        ans2 = rightMost(l,r)

        if ans1 > ans2:
            return [-1,-1]

        if ans1 == ans2 and A[ans1] == B:
            return [ans1,ans2]
        else:
            return [-1,-1]




sol = Solution()
# sol.searchRange([5,7,7,8,8,10],8)
# sol.searchRange([1,2,4,4,5], 3)
print(sol.searchRange([1,2,5,6], 10))
print(sol.searchRange([1,2,5,6], 1))

            
