
## Lowest common ancestor of binary tree
- Ref: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency

### Approach
- Trees

```py
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        if root.val in (node.val for node in nodes):
            return root

        left = TreeNode(None) 
        right = TreeNode(None)

        if root.left:
            left = self.lowestCommonAncestor(root.left, nodes)
        if root.right:
            right = self.lowestCommonAncestor(root.right, nodes)
        
        if left.val and right.val:
            return root

        if left.val:
            return left
        return right
```
        
        