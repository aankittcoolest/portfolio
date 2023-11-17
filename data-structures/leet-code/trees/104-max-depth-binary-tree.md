
## Maximum depth binary tree
- Ref: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150

### Approach
- Recursion
- DFS (stack)
- BFS (queue)

```py
from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.maxDepthDFS(root)

    # Recursive Approach
    def maxDepthRecursive(self, root: Optional[TreeNode], depth) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepthRecursive(root.left,depth), self.maxDepthRecursive(root.right,depth))

    # BFS Approach(using Queue)
    def maxDepthBFS(self, root: Optional[TreeNode]):
        q = deque([root])
        level = 0

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level

    # DFS Approach(using Stack) + PreOrder
    def maxDepthDFS(self, root: Optional[TreeNode]):
        stack = [[root, 1]]
        res = 0
        while stack:
            [node, depth] = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.right,depth+1])
                stack.append([node.left,depth+1])
        return res

        


left = TreeNode(15)
right = TreeNode(7)
right = TreeNode(20,left,right)
left = TreeNode(9)
root = TreeNode(3,left,right)

sol = Solution()
print(sol.maxDepth(root))

        
```