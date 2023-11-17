
## Remove nth element from linked list
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/128079/homework/problems/39/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/040-remove-nth-element-from-linked-list-question.png)

### Approach
- calculate length of linked list in one iteration.

```py
class Solution:

    def delete_node(self, head, position):
        tempNode = head
        count = 1

        # head situation
        if position == 1:
            head = tempNode.next
            return head

        prevNode = None
        while tempNode:
            if count == position:
                prevNode.next = tempNode.next
                return head
            prevNode = tempNode
            tempNode = tempNode.next
            count += 1

    def removeNthFromEnd(self, A, B):
        length_ll = 0
        head = A

        while head:
            length_ll += 1
            head = head.next

        idx_to_be_removed = length_ll-B+1
        if idx_to_be_removed <= 0:
            A = self.delete_node(A, 1)
        else:
            A = self.delete_node(A, idx_to_be_removed)

        return A
```