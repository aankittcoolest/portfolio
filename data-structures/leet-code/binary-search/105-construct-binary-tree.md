

## Construct binary tree from preorder and inorder traversal
- Ref:  https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/?envType=study-plan-v2&envId=top-interview-150

### Approach
- recursion

```py
from typing import List, Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root


left = TreeNode(15)
right = TreeNode(7)
rightParent = TreeNode(20, left, right)
leftParent = TreeNode(9)
root = TreeNode(3, left, right)

sol = Solution()
sol.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
```