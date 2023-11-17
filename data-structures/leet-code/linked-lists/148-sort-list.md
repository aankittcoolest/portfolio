
## Sort list
- Ref: https://leetcode.com/problems/sort-list/description/?envType=study-plan-v2&envId=top-interview-150

### Approach
- linked list
- merge sort

```py
# Definition for singly-linked list.
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

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
    def sortList(self, A):
        if not A or not A.next:
            return A

        left = A
        right = self.getMid(A)
        tmp = right.next
        right.next = None
        right = tmp

        left = self.sortList(left)
        right = self.sortList(right)

        return self.mergeTwoLists(left,right)
    
    def getMid(self,head):
        slow,fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def mergeTwoLists(self, A, B):
        dummy = tail = ListNode(-1)
        while A and B:
            if A.val < B.val:
                tail.next = A
                A = A.next
            else:
                tail.next = B
                B = B.next
            tail = tail.next

        if A:
            tail.next = A
        
        if B:
            tail.next = B
        return dummy.next


insert_node(1, 4)
insert_node(2, 2)
insert_node(3, 1)
insert_node(4, 3)
insert_node(5, 5)
print_ll()

sol = Solution()
head = sol.sortList(head)
print_ll()
```