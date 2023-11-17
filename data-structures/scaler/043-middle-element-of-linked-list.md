

## Find middle element of linked list
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/127931/assignment/problems/4370/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/043-middle-element-of-linked-list-question.png)

### Approach
- slow and fast pointers

```py
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


head = None


def insert_node(position, value):
    global head
    cur_node = head

    node = ListNode(value)

    if position == 1:
        if head == None:
            head = node
            return
        else:
            node.next = head
            head = node
            return

    idx = 2
    while cur_node:
        if idx == position:
            node.next = cur_node.next
            cur_node.next = node
            return
        cur_node = cur_node.next
        idx += 1


def delete_node(position):
    global head
    cur_node = head

    if position == 1:
        head = head.next
        return

    idx = 2
    while cur_node:
        if position == idx:
            if cur_node.next:
                if cur_node.next.next:
                    cur_node.next = cur_node.next.next
                else:
                    cur_node.next = None
            return
        cur_node = cur_node.next
        idx += 1

    pass


def print_ll():
    global head
    cur_node = head
    nodes = []

    while cur_node:
        nodes.append(str(cur_node.val))
        cur_node = cur_node.next

    print(" ".join(nodes))


class Solution:
    # @param A : head node of linked list
    # @return an integer
    def solveSimple(self, A):
        head = A
        ln = 0

        while head:
            ln += 1
            head = head.next

        mid = (ln//2) + 1

        head = A
        ln = 0
        while head:
            ln += 1
            if mid == ln:
                return head
            head = head.next

    def solve(self, A):
        if not A or not A.next:
            return A

        slow = fast = A
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.val


sol = Solution()

insert_node(1, 10)
insert_node(2, 20)
insert_node(3, 30)
insert_node(4, 40)
insert_node(5, 50)
node = sol.solve(head)
print(node)
```
