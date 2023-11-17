
## Remove duplicates from sorted list
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/128079/homework/problems/37/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/040-remove-duplicates-from-sorted-list-question.png)

### Approach
- adjust pointers

```py
class Solution:
    def deleteDuplicates(self, A):
        head = A
        prevNode = A

        while head:
            if head.val != prevNode.val:
                prevNode.next = head
                prevNode = head
            head = head.next
        prevNode.next = None
        return A


insert_node(1, 1)
insert_node(2, 1)
insert_node(3, 2)
insert_node(4, 2)
insert_node(5, 20)
insert_node(6, 20)
print_ll()

sol = Solution()
head = sol.deleteDuplicates(head)
print_ll()
```