
## Add two numbers
- Ref: https://leetcode.com/problems/add-two-numbers/description/?envType=study-plan-v2&envId=top-interview-150

### Approach
- maths

```py
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def getLen(lst):
            ln = 0
            while lst:
                ln += 1
                lst = lst.next
            return ln

        l1_len = getLen(l1)
        l2_len = getLen(l2)

        if l2_len > l1_len:
            l1, l2 = l2, l1

        head = l1

        carry = 0
        while l1 and l2:
            sm = l1.val + l2.val
            if carry:
                sm += carry
                carry = 0
            if sm//10 == 1:
                carry = 1
            l1.val = sm % 10
            if l1.next is None and carry:
                node = ListNode(carry)
                l1.next = node
                carry = 0
            l1 = l1.next
            l2 = l2.next

        while l1:
            sm = l1.val
            if carry:
                sm += carry
                carry = 0
            if sm//10 == 1:
                carry = 1
            l1.val = sm % 10
            if l1.next is None and carry:
                node = ListNode(carry)
                l1.next = node
                carry = 0
            l1 = l1.next

        return head
```