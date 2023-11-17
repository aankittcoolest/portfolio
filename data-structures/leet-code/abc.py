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
	# @param B : head node of linked list
	# @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        ln_A = self.getLen(A)
        ln_B = self.getLen(B)

        if ln_B > ln_A:
            A,B = B,A
        head = A
        carry = 0
        trackNode = A
        while A:
            sm = A.val + B.val + carry

            if sm > 10:
                A.val = sm %10
                carry = 1
            else:
                A.val = sm
                carry = 0
            trackNode = A
            A = A.next
            B = B.next
        
        while carry and A:
            sm = A.val +  carry
            if sm > 10:
                A.val = sm %10
            else:
                A.val = sm
                carry = 0
            trackNode = A

        if carry:
            node = ListNode(carry)
            trackNode.next = node

        return head

    
    def getLen(self,A):
        node = A

        count = 0
        while node:
            node = node.next
            count +=1 

        return count


insert_node(1, 1)
insert_node(2, 2)
insert_node(3, 3)
insert_node(4, 4)
insert_node(5, 5)
insert_node(6, 6)
print_ll()

sol = Solution()
head = sol.addTwoNumbers(head,head)
print_ll()