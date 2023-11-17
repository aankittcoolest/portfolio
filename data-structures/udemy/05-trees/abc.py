# Level order traversal is done using queue

from typing import Optional
from typing import List
from collections import deque


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
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(l, r):
            if l > r:
                return None

            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = helper(l, mid-1)
            root.right = helper(mid+1, r)
            return root

        ans = helper(0, len(nums)-1)

        # This method can be used to verify the output
        # self.inOrderTraversal(ans)
        return ans

    def preOrderTraversal(self, node):
        if node is None:
            return

        print(node.val)
        self.preOrderTraversal(node.left)
        self.preOrderTraversal(node.right)

    def inOrderTraversal(self, node):
        queue = deque([])
        queue.appendleft(node)

        items = []
        while len(queue) > 0:
            item = queue.pop()
            if item:
                items.append(item.val)
                if item.left and item.right:
                    queue.appendleft(item.left)
                    queue.appendleft(item.right)
                elif item.left and item.right is None:
                    queue.appendleft(item.left)
                    queue.appendleft(None)
                elif item.right and item.left is None:
                    queue.appendleft(None)
                    queue.appendleft(item.right)
            else:
                items.append(None)

        print(items)


def example():
    sol = Solution()
    result = sol.sortedArrayToBST([-10, -3, 0, 5, 9])
    # result = sol.sortedArrayToBST([1,3])
    # sol.preOrderTraversal(result)


example()
