

## Invert a binary tree
- Ref: https://leetcode.com/problems/invert-binary-tree/?envType=study-plan-v2&envId=top-interview-150


### Approach
- tree-traversal
- Reverse left and right

```py
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root = self.invert(root)

    def invert(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invert(root.left)
        self.invert(root.right)
        return root

    def inOrderTraversal(self, root: Optional[TreeNode]):
        if not root:
            return

        self.inOrderTraversal(root.left)
        print(root.val)
        self.inOrderTraversal(root.right)



left = TreeNode(1)
right = TreeNode(3)
leftParent = TreeNode(2,left,right)

left = TreeNode(6)
right = TreeNode(9)
rightParent = TreeNode(7,left,right)

root = TreeNode(4,leftParent,rightParent)

sol = Solution()
sol.invertTree(root)
        
```