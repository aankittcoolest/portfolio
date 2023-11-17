

## Figure out if two trees are same trees
- https://leetcode.com/problems/same-tree/description/


## Approach
- Here we do "inorder" traversal on both trees and figure out if both generated lists are equal.
- Here we keep track of null leaves also.


```py
from typing import Optional
from typing import List


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.inOrderTraversal(p) == self.inOrderTraversal(q)

    def inOrderTraversal(self, node: Optional[TreeNode]) -> List:
        if node is None:
            return
        list = []
        output = self.inOrderTraversal(node.left)
        list.append(node.val)
        if output is None:
            list.append(None)
        else:
            list.extend(output)
        output = self.inOrderTraversal(node.right)
        if output is None:
            list.append(None)
        else:
            list.extend(output)
        return list

def example1Equal():
    leftNode = TreeNode(3)
    rightNode = TreeNode(2)
    rootNode = TreeNode(1,leftNode,rightNode)
    p = rootNode

    leftNode = TreeNode(3)
    rightNode = TreeNode(2)
    rootNode = TreeNode(1,leftNode,rightNode)
    q = rootNode

    solution = Solution()
    sol = solution.isSameTree(p,q)
    print(sol)

def example2NotEqual():
    leftNode = TreeNode(2)
    rightNode = TreeNode(3)
    rootNode = TreeNode(1,leftNode,rightNode)
    p = rootNode

    leftNode = TreeNode(3)
    rightNode = TreeNode(2)
    rootNode = TreeNode(1,leftNode,rightNode)
    q = rootNode

    solution = Solution()
    sol = solution.isSameTree(p,q)
    print(sol)

example1Equal()
example2NotEqual()
```