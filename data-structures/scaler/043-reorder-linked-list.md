## Reorder linked list
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/127931/homework/problems/33/?navref=cl_pb_nv_tb

### Approach
- linked list

```py
class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
    def reorderList(self, A):
        left = A
        right = self.findMid(A)
        tmp = right.next
        right.next = None
        right = tmp

        right = self.reverseList(right)

        while right:
            tmp = left.next
            left.next = right
            left = tmp

            tmp = right.next
            right.next = left
            right = tmp

        return A

    def findMid(self,A):
        slow,fast = A,A.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self,A):
        curr = A
        next, prev = None,None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        A = prev
        return A
```