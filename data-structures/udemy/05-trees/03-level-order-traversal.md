

## Level Order Traversal
- Level order traversal on a binary tree is done by using queue.


### Approach


```py
## Level order traversal is done using queue

from typing import Optional
from typing import List

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) > 0:
            return self.items.pop(0)
        return None

    def peek(self):
        if len(self.items) > 0:
            return self.items[0]
        return None

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        return False

    def getTotal(self):
        return len(self.items)


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return
        queue = Queue()
        queue.enqueue(root)

        answer = []
        while not queue.isEmpty():
            list = []
            qLen = queue.getTotal()
            for i in range(qLen):
                item = queue.dequeue()
                list.append(item.val)
                if item.left:
                    queue.enqueue(item.left)
                if item.right:
                    queue.enqueue(item.right)
            answer.append(list)
        return answer

def example():
    teaNode = TreeNode("Tea")
    coffeeNode = TreeNode("Coffee")
    leftNode = TreeNode("Hot", teaNode, coffeeNode)
    rightNode = TreeNode("Cold")
    rootNode = TreeNode("Drinks",leftNode,rightNode)

    sol = Solution()
    ans = sol.levelOrder(rootNode)
    print(ans)

example()
```