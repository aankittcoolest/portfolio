

## Reverse linked list
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/128079/assignment/problems/40/?navref=cl_pb_nv_tb

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/040-reverse-linked-list-question.png)

### Approach
- Three pointers

```py
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


head = None


def insert_node(position, value):
    global head
    tempNode = head
    prevNode = None
    node = ListNode(value)
    count = 1
    if position == 1:
        if head is None:
            head = node
        else:
            node.next = head
            head = node
        return
    else:
        while tempNode:
            if count == position:
                prevNode.next = node
                node.next = tempNode
                return
            prevNode = tempNode
            tempNode = tempNode.next
            count += 1

    # tail situaion
    if position == count:
        prevNode.next = node

    pass


def delete_node(position):
    global head
    tempNode = head
    count = 1

    # head situation
    if position == 1:
        head = tempNode.next
        return

    prevNode = None
    while tempNode:
        if count == position:
            prevNode.next = tempNode.next
            return
        prevNode = tempNode
        tempNode = tempNode.next
        count += 1


def print_ll():
    global head
    tempNode = head
    result = []
    while tempNode:
        result.append(str(tempNode.val))
        tempNode = tempNode.next

    print(" ".join(result))


def reverseList():
    global head
    curNode = head
    prevNode = None
    nextNode = None

    while curNode:
        nextNode = curNode.next
        curNode.next = prevNode
        prevNode = curNode
        curNode = nextNode

    head = prevNode


insert_node(1, 10)
insert_node(2, 30)
insert_node(3, 50)
insert_node(2, 20)
print_ll()
# delete_node(3)
# delete_node(3)
# delete_node(4)
# print_ll()
# insert_node(1, 5)
# print_ll()
reverseList()
print_ll()
```
