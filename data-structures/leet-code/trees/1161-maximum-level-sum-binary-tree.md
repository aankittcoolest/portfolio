
## Maximum level sum binary tree
- Ref: https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/

### Approach
- binary tree BFS

```py
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        sum = 0
        mxSum = float("-inf")
        ans = 0
        level = 0

        while q:
            sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
            if sum > mxSum:
                mxSum = sum
                ans = level

        return ans


sol = Solution()

left = TreeNode(7)
right = TreeNode(-8)

leftParent = TreeNode(1, left, right)

left = TreeNode(-7)
right = TreeNode(9)
rightParent = TreeNode(0, left, right)

root = TreeNode(1, leftParent, rightParent)
print(sol.maxLevelSum(root))
```