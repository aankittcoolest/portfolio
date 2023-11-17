
## Remove loop from linked list
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/127931/assignment/problems/4226/?navref=cl_pb_nv_tb

### Approach
- Warshall Floyd Algorithm
- Slow fast pointers

```py
# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        slow,fast = A, A.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        if slow != fast:
            return A

        slow = A
        while slow != fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = None
        return A
```