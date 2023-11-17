
## Merge two sorted linked list
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/127931/assignment/problems/36/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/043-merge-two-sorted-linked-list-question.png)

### Approach
- two pointers

```py
class Solution:
    def mergeTwoLists(self, A, B):
        if A == None:
            return B

        if B == None:
            return A

        head = None

        if A.val < B.val:
            head = A
            A = A.next
        else:
            head = B
            B = B.next

        node = head

        while A and B:
            if A.val < B.val:
                node.next = A
                A = A.next
            else:
                node.next = B
                B = B.next
            node = node.next

        while A:
            node.next = A
            A = A.next
            node = node.next

        while B:
            node.next = B
            B = B.next
            node = node.next

        return head
```